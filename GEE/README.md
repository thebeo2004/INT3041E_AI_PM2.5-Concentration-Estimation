# Dữ liệu trích xuất từ Google Earth Engine

Ngoài dữ liệu được cung cấp, nhóm đã thử trích xuất thêm các đặc trưng từ Google Earth Engine (GEE) để tăng cường khả năng dự đoán Chỉ số Chất lượng Không khí (AQI). Dữ liệu bổ sung được trích xuất cho từng trạm (dựa trên ID và tọa độ gốc được cung cấp) và bao gồm các giá trị đặc trưng trong từng ngày trong khoảng thời gian từ năm 2019 đến 2024.

Dưới đây là mô tả chi tiết về các đặc trưng đã trích xuất và lý do nhóm lựa chọn chúng.

## 1. Đặc trưng từ Sentinel-5P
> Sơ lược về Sentinel-5P: Sentinel-5 Precursor (Sentinel-5P) là một vệ tinh quan sát Trái Đất thuộc chương trình Copernicus của Liên minh Châu Âu, được phóng vào ngày 13 tháng 10 năm 2017. Vệ tinh này mang theo thiết bị TROPOMI (Tropospheric Monitoring Instrument), cho phép đo lường các khí trong khí quyển như CO, NO2, O3, SO2, CH4 và các chỉ số aerosol với độ phân giải không gian cao (khoảng 3.5 x 5.5 km²) và tần suất hàng ngày. Dữ liệu từ Sentinel-5P được sử dụng rộng rãi trong nghiên cứu chất lượng không khí và biến đổi khí hậu, cung cấp thông tin quan trọng về các chất ô nhiễm liên quan đến PM2.5 và AQI.

Nhóm đã trích xuất 8 đặc trưng từ bộ dữ liệu [Sentinel-5P trên GEE](https://developers.google.com/earth-engine/datasets/catalog/sentinel-5p?hl=vi), tương ứng với các năm từ 2019 đến 2024. Các đặc trưng này được lấy từ các bộ dữ liệu liên quan đến khí quyển, bao gồm UVAI, CLOUD, CO, CO2, NO2, O3, SO2 và CH4. Với mỗi bộ dữ liệu, nhóm chọn một band quan trọng nhất làm đặc trưng đại diện.
### 1.1. [UVAI](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_AER_AI?hl=vi)
- Mô tả bộ dữ liệu: Bộ dữ liệu này cung cấp thông tin về chỉ số hấp thụ aerosol (Aerosol Index) dựa trên phép đo tia UV từ vệ tinh Sentinel-5P, phản ánh mức độ aerosol trong khí quyển.
- Band được chọn: absorbing_aerosol_index
- Mô tả band: Band này đo lường chỉ số hấp thụ aerosol, biểu thị sự hiện diện của các hạt aerosol hấp thụ tia UV như bụi mịn hoặc khói.
- Lý do lựa chọn: Chỉ số hấp thụ aerosol được tính dựa trên sự khác biệt quang phổ giữa bước sóng UV (340 nm và 380 nm), có khả năng phát hiện các hạt bụi mịn (PM2.5) và khói từ cháy rừng hoặc hoạt động công nghiệp, vốn là thành phần chính ảnh hưởng đến AQI.

### 1.2. [CLOUD](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_CLOUD?hl=vi)
- Mô tả bộ dữ liệu: Bộ dữ liệu này cung cấp thông tin về đặc tính của mây (độ che phủ, độ cao, v.v.) từ phép đo của Sentinel-5P, liên quan đến điều kiện khí tượng.
- Band được chọn: cloud_fraction
- Mô tả band: Band này biểu thị tỷ lệ che phủ mây trong khí quyển tại thời điểm quan sát.
- Lý do lựa chọn: Độ che phủ mây ảnh hưởng đến quá trình khuếch tán và lắng đọng của các hạt aerosol và khí ô nhiễm. Khi mây dày, sự khuếch tán giảm, dẫn đến tích tụ chất ô nhiễm gần mặt đất, làm tăng nồng độ PM2.5.

### 1.3 [CO](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_CO?hl=vi)
- Mô tả bộ dữ liệu: Bộ dữ liệu này đo lường nồng độ khí CO (carbon monoxide) trong khí quyển, chủ yếu từ các nguồn khí thải công nghiệp và giao thông.
- Band được chọn: CO_column_number_density
- Mô tả band: Band này biểu thị mật độ cột khí CO trong khí quyển, tính bằng mol/m².
- Lý do lựa chọn: CO là sản phẩm của quá trình đốt cháy không hoàn toàn, thường đồng phát sinh với các hạt bụi mịn từ cùng nguồn (như khí thải xe cộ). Dữ liệu này cung cấp thông tin bổ sung về mức độ ô nhiễm từ các nguồn phát thải liên quan đến PM2.5.
### 1.4. [CO2](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_HCHO?hl=vi)
- Mô tả bộ dữ liệu: Bộ dữ liệu này thực chất đo lường formaldehyde (HCHO), được dùng làm proxy gián tiếp cho CO2 vì dữ liệu CO2 trực tiếp không có sẵn từ Sentinel-5P.
- Band được chọn: tropospheric_HCHO_column_number_density
- Mô tả band: Band này đo mật độ cột khí HCHO trong tầng đối lưu (troposphere), tính bằng mol/m², tập trung vào phần khí quyển gần mặt đất nơi các quá trình hóa học ô nhiễm xảy ra.
- Lý do lựa chọn: HCHO được tạo ra từ quá trình oxy hóa các hợp chất hữu cơ dễ bay hơi (VOCs) và CO2 trong khí quyển dưới tác động của ánh sáng mặt trời. Dữ liệu này phản ánh mức độ hoạt động hóa học liên quan đến ô nhiễm không khí, hỗ trợ dự đoán PM2.5.
### 1.5. [NO2](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_NO2?hl=vi)
- Mô tả bộ dữ liệu: Bộ dữ liệu này cung cấp thông tin về nồng độ khí NO2 (nitrogen dioxide), một chất ô nhiễm chính từ khí thải phương tiện và nhà máy.
- Band được chọn: tropospheric_NO2_column_number_density
- Mô tả band: Band này đo mật độ cột khí NO2 trong tầng đối lưu (troposphere), tính bằng mol/m², tập trung vào phần khí quyển gần mặt đất nơi ô nhiễm xảy ra.
- Lý do lựa chọn: NO2 trong tầng đối lưu tham gia vào các phản ứng quang hóa với ánh sáng mặt trời, tạo ra hạt nitrate (một thành phần của PM2.5) thông qua quá trình oxy hóa. Band này được chọn vì nó phản ánh chính xác nồng độ NO2 ở vùng khí quyển liên quan trực tiếp đến ô nhiễm mặt đất.
### 1.6. [O3](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_O3?hl=vi)
- Mô tả bộ dữ liệu: Bộ dữ liệu này đo lường nồng độ khí ozone (O3) trong khí quyển, đặc biệt ở tầng đối lưu.
- Band được chọn: O3_column_number_density
- Mô tả band: Band này biểu thị mật độ cột khí ozone, tính bằng mol/m².
- Lý do lựa chọn: Ozone tầng đối lưu được hình thành từ phản ứng quang hóa giữa NO2 và VOCs dưới ánh sáng mặt trời, đồng thời thúc đẩy quá trình oxy hóa tạo hạt thứ cấp trong PM2.5. Dữ liệu này bổ sung thông tin về các phản ứng hóa học liên quan đến ô nhiễm.
### 1.7. [SO2](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_SO2?hl=vi)
- Mô tả bộ dữ liệu: Bộ dữ liệu này cung cấp thông tin về nồng độ khí SO2 (sulfur dioxide), chủ yếu từ hoạt động đốt nhiên liệu hóa thạch.
- Band được chọn: SO2_column_number_density
- Mô tả band: Band này đo mật độ cột khí SO2 trong khí quyển, tính bằng mol/m².
- Lý do lựa chọn: SO2 phản ứng với hơi nước và oxy trong khí quyển để tạo thành hạt sulfate, một thành phần chính của PM2.5. Band này được chọn vì nó cung cấp dữ liệu trực tiếp về nguồn phát thải liên quan đến quá trình hình thành bụi mịn.
### 1.8. [CH4](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_OFFL_L3_CH4?hl=vi)
- Mô tả bộ dữ liệu: Bộ dữ liệu này đo lường nồng độ khí metan (CH4), một khí nhà kính quan trọng trong khí quyển.
- Band được chọn: CH4_column_number_density
- Mô tả band: Band này biểu thị mật độ cột khí CH4, tính bằng mol/m².
- Lý do lựa chọn: CH4 tham gia vào các phản ứng hóa học trong khí quyển, đặc biệt là với gốc hydroxyl (OH), ảnh hưởng đến khả năng oxy hóa các chất ô nhiễm khác như VOCs, từ đó tác động gián tiếp đến sự hình thành PM2.5.
## 2. Đặc trưng bổ sung: NDVI và AOD
Ngoài các đặc trưng từ Sentinel-5P, nhóm trích xuất thêm 2 đặc trưng từ các bộ dữ liệu khác trên GEE để bổ sung thông tin về NDVI và AOD.
### 2.1. [NDVI](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MOD13A2?hl=vi)
- Mô tả bộ dữ liệu: Bộ dữ liệu MOD13A2 cung cấp chỉ số thực vật từ vệ tinh Terra MODIS, với chu kỳ 16 ngày và độ phân giải 1 km.
- Band được chọn: NDVI
- Mô tả band: Band này là chỉ số chênh lệch thực vật chuẩn hóa, đo lường mức độ phủ xanh của thảm thực vật.
- Lý do lựa chọn: Thảm thực vật hấp thụ CO2 qua quang hợp và giữ lại các hạt bụi mịn trên lá, làm giảm nồng độ PM2.5 trong không khí. NDVI được chọn vì nó là chỉ số tiêu chuẩn để đánh giá mật độ thực vật.
### 2.2. [OAD](https://developers.google.com/earth-engine/datasets/catalog/MODIS_061_MCD19A2_GRANULES?hl=vi)
- Mô tả bộ dữ liệu: Bộ dữ liệu MCD19A2 cung cấp độ sâu quang học aerosol (AOD) hàng ngày từ vệ tinh Terra và Aqua MODIS, độ phân giải 1 km.
- Band được chọn: Optical_Depth_047
- Mô tả band: Band này đo độ sâu quang học aerosol ở bước sóng 470 nm, biểu thị lượng hạt aerosol trong khí quyển.
- Lý do lựa chọn: AOD tại bước sóng 470 nm có tương quan cao với nồng độ PM2.5 đo được trên mặt đất, do nó phản ánh mức độ tán xạ và hấp thụ ánh sáng bởi các hạt aerosol trong khí quyển.

## 3. Lựa chọn đặc trưng sau khi trích xuất
Mặc dù nhóm đã trích xuất 10 đặc trưng ban đầu được đánh giá là có ảnh hưởng đến AQI, sau khi kiểm tra dữ liệu, một số đặc trưng bị thiếu giá trị nghiêm trọng. Việc imputation cho các đặc trưng thiếu quá nhiều dữ liệu có thể làm giảm độ tin cậy của mô hình. Do đó, nhóm quyết định loại bỏ 2 đặc trưng là SO2 và AOD vì tỷ lệ thiếu dữ liệu cao, không phù hợp để sử dụng trong phân tích.

Như vậy, sau quá trình trích xuất và kiểm tra, nhóm chốt lại 8 đặc trưng cuối cùng bao gồm: UVAI, CLOUD, CO, CO2 (HCHO), NO2, O3, CH4 và NDVI.