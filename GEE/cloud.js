// Tạo danh sách tọa độ từ bảng
var table = ee.FeatureCollection('projects/praxis-surface-440006-f7/assets/data1')
  .distinct(['lon', 'lat']);

// Hàm tạo danh sách ngày cho một năm, bao gồm 31/12
var generateDateList = function(year) {
  var startDate = ee.Date(year + '-01-01');
  var endDate = ee.Date(year + '-12-31');
  // Không trừ 1 để bao gồm cả ngày cuối cùng
  return ee.List.sequence(0, endDate.difference(startDate, 'day'))
    .map(function(n) { return startDate.advance(n, 'day'); });
};

// Hàm xử lý và xuất dữ liệu cho một năm
var processYear = function(year) {
  var dateList = generateDateList(year);
  
  // Tạo FeatureCollection cho năm đó
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
  
  // Kết nối với Sentinel-5P
  var collection = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_CLOUD')
    .select('cloud_fraction')
    .filterDate(year + '-01-01', ee.Date(year + '-12-31').advance(1, 'day')); // Bao gồm đến 00:00 ngày 1/1 năm sau
  
  // Hàm trích xuất CO
  var extractCOValues = function(feature) {
    var point = feature.geometry();
    var date = ee.Date(feature.get('date'));
    var dailyImage = collection
      .filterDate(date, date.advance(1, 'day'))
      .mean();
    
    var coValue = dailyImage.reduceRegion({
      reducer: ee.Reducer.mean(),
      geometry: point,
      scale: 1113.2,
      maxPixels: 1e9
    }).get('cloud_fraction');
    
    return ee.Feature(null, {
      'lon': feature.get('lon'),
      'lat': feature.get('lat'),
      'date': date.format('YYYY-MM-dd'),
      'ID': feature.get('ID'),
      'cloud_fraction': coValue
    });
  };
  
  // Áp dụng và xuất
  var sampledValues = pointCollection.map(extractCOValues, true);
  Export.table.toDrive({
    collection: sampledValues,
    description: 'CLOUD_' + year,
    folder: 'DATA-AI',
    fileFormat: 'CSV',
    selectors: ['lon', 'lat', 'date', 'ID', 'cloud_fraction']
  });
};

// Xử lý từng năm
processYear('2019');
processYear('2020');
processYear('2021');
processYear('2022');
processYear('2023');
processYear('2024');
