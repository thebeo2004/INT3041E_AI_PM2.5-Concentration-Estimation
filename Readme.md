# Ước Lượng Chỉ Số AQI 

Dự án này nhằm mục đích **ước lượng chỉ số chất lượng không khí (AQI)** bằng cách sử dụng các mô hình học máy và dữ liệu được trích xuất từ nhiều nguồn khác nhau, bao gồm dữ liệu khí tượng, dữ liệu vệ tinh và các tập dữ liệu đã được nội suy. Dự án sử dụng các công cụ như **Google Earth Engine (GEE)**, **PyCaret** và các framework học máy để tiền xử lý dữ liệu, huấn luyện mô hình và đánh giá hiệu suất.

## Các Tính Năng Chính

1. **Trích Xuất Dữ Liệu**  
   - Dữ liệu khí tượng và dữ liệu vệ tinh được trích xuất từ **Google Earth Engine**.  
   - Các đặc trưng bao gồm: **UVAI**, **CLOUD**, **CO**, **NO₂**, **O₃**, **CH₄** và **NDVI**.

2. **Nội Suy Dữ Liệu Thiếu**  
   - Giá trị thiếu được xử lý bằng các phương pháp như **KNN**, **trung bình động có trọng số tuyến tính** và **phương pháp không gian–thời gian**.

3. **Huấn Luyện Mô Hình**  
   - Các mô hình học máy được sử dụng bao gồm **Random Forest**, **LightGBM**, **Extra Trees**, **Gradient Boosting**,...  
   - Tối ưu siêu tham số được thực hiện bằng `RandomizedSearchCV`.

4. **Đánh Giá Mô Hình**  
   - Sử dụng các chỉ số như **accuracy**, **F1-score**, **AUC**, **Recall**, **Precision**, **Kappa**, **MCC** để đánh giá hiệu suất mô hình.  
   - Các mô hình tốt nhất được lưu dưới dạng tệp `.pkl` để phục vụ triển khai.

5. **Trực Quan Hóa**  
   - Tạo biểu đồ trực quan thể hiện **tầm quan trọng của đặc trưng**, **kết quả phân loại**, và **phân bố dữ liệu**.
