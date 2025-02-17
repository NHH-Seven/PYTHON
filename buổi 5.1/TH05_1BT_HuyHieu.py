#Bài 1: trang 13
import numpy as np
vector_a = np.arange(1,31)
print(vector_a)
a_le = vector_a[1::2]
a_chan = vector_a[0::2]
a_3 = vector_a[2::3]
print('cac phan tu le cua vector_a:',a_le)
print('cac phan tu chan cua vector_a:',a_chan)
print('cac phan tu chia het cho 3 cua vector_a:',a_3)
#Bài 2: trang 30
path = 'c:\\Users\\zhieu\\OneDrive\\Documents\\Python\\buổi 5.1\\data_bmi.txt'
bmi = np.loadtxt(path)
print(bmi)
#Bài 2.1: trang 31  
cc , cn = np.hsplit(bmi,2)
print('vector chieu cao : \n',cc.ravel())
print('vector can nang : \n',cn.ravel())
#Bài 2.2: trang 33
print('vector chieu cao chuyen tu cm qua m va binh phuong cac phan tu: \n',np.power(cc*0.01,2).ravel())
#Bài 2.3: trang 34
bmi1 = (cc/cn).ravel()
v_BMI = np.around(bmi1,1)
print('chi so BMI : \n', v_BMI)
#Bài 2.4: trang 35
print('tang dan: \n',np.sort(v_BMI))
print('giam dan: \n',-np.sort(-v_BMI))
#Bài 2.5: trang 36
import pandas as pd # type: ignore
import numpy as np

# Đọc dữ liệu từ file CSV


# Xử lý dữ liệu
bmi_data = []
for line in bmi:
    height, weight = map(float, line.split())
    bmi_data.append((height, weight))

# Hàm tính BMI
def calculate_bmi(height, weight):
    return weight / (height ** 2)

# Phân loại BMI
categories = {
    "Gầy": 0,
    "Bình thường": 0,
    "Thừa cân": 0,
    "Béo phì": 0
}

# Tính toán và phân loại
for height, weight in bmi_data:
    bmi = calculate_bmi(height, weight)
    if bmi < 18.5:
        categories["Gầy"] += 1
    elif 18.5 <= bmi < 25:
        categories["Bình thường"] += 1
    elif 25 <= bmi < 30:
        categories["Thừa cân"] += 1
    else:
        categories["Béo phì"] += 1

# In kết quả
for category, count in categories.items():
    print(f"{category}: {count}")
