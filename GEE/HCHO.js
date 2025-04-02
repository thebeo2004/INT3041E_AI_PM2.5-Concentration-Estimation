// Tạo danh sách tọa độ từ bảng
var table = ee.FeatureCollection('projects/praxis-surface-440006-f7/assets/data1')
  .distinct(['lon', 'lat']);

// Hàm tạo danh sách ngày cho năm 2021, bao gồm 31/12
var generateDateList = function() {
  var startDate = ee.Date('2024-01-01');
  var endDate = ee.Date('2024-12-31');
  return ee.List.sequence(0, endDate.difference(startDate, 'day'))
    .map(function(n) { return startDate.advance(n, 'day'); });
};

// Xử lý dữ liệu cho năm 2021
var dateList = generateDateList();

// Tạo FeatureCollection cho năm 2021
var pointCollection = table.map(function(feature) {
  var lon = ee.Number(feature.get('lon'));
  var lat = ee.Number(feature.get('lat'));
  var point = ee.Geometry.Point([lon, lat]);
  return ee.FeatureCollection(
    dateList.map(function(date) {
      return ee.Feature(point, {
        'date': ee.Date(date),
        'ID': feature.get('ID'),
        'lon': lon,
        'lat': lat
      });
    })
  );
}).flatten();

// Kết nối với Sentinel-5P HCHO
var collection = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_HCHO')
  .select('tropospheric_HCHO_column_number_density')
  .filterDate('2024-01-01', ee.Date('2024-12-31').advance(1, 'day'));

// Hàm trích xuất HCHO
var extractHCHOValues = function(feature) {
  var point = feature.geometry();
  var date = ee.Date(feature.get('date'));
  var dailyImage = collection
    .filterDate(date, date.advance(1, 'day'))
    .mean();
  
  // Trích xuất giá trị với xử lý trường hợp thiếu dữ liệu
  var hchoDict = dailyImage.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: point,
    scale: 1113.2,
    maxPixels: 1e9
  });
  
  // Kiểm tra khóa và trả về null nếu không có dữ liệu
  var hchoValue = ee.Algorithms.If(
    hchoDict.contains('tropospheric_HCHO_column_number_density'),
    hchoDict.get('tropospheric_HCHO_column_number_density'),
    null
  );
  
  return ee.Feature(null, {
    'lon': feature.get('lon'),
    'lat': feature.get('lat'),
    'date': date.format('YYYY-MM-dd'),
    'ID': feature.get('ID'),
    'tropospheric_HCHO_column_number_density': hchoValue
  });
};

// Áp dụng và xuất
var sampledValues = pointCollection.map(extractHCHOValues, true);
Export.table.toDrive({
  collection: sampledValues,
  description: 'Formaldehyde_2024',
  folder: 'DATA-AI',
  fileFormat: 'CSV',
  selectors: ['lon', 'lat', 'date', 'ID', 'tropospheric_HCHO_column_number_density']
});