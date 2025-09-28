import pandas as pd
import matplotlib.pyplot as plt

# Hàm chính để chạy ứng dụng
if __name__ == '__main__':
    # Đọc dữ liệu từ file CSV
    data = pd.read_csv('data.csv')
    
    # Hiển thị thông tin cơ bản về dữ liệu
    print(data.info())
    
    # Ví dụ: Phân tích dân số theo vùng miền
    region_counts = data['region'].value_counts()
    print(region_counts)
    
    # Biểu đồ
    region_counts.plot(kind='bar')
    plt.title('Phân bố dân số theo vùng miền')
    plt.xlabel('Vùng miền')
    plt.ylabel('Số lượng')
    plt.show()