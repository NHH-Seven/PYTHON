#bai 6
chuoi = str(input('nhap chuoi :'))
if chuoi== 'U' or chuoi== 'E' or chuoi== 'O' or chuoi== 'A' or chuoi== 'I':
    print('nguyen am')
else:
    print('phu am')
#bai 7
cao = int(input('nhap chieu cao :'))
nang = int(input('nhap nang :'))
BMI = nang / (cao^2)
if BMI < 18.5:
    print('Underwelght')
elif BMI < 25:
    print('Normal weight')
elif BMI < 30:
    print('Overweight')
else:
    print('Obese')
#bai 8
thang = int(input('nhap thang :'))
if thang == 1 or thang == 2 or thang == 3 :
    print ('ban sinh vao mua xuan')
elif thang == 4 or thang == 5 or thang == 6 :
    print ('ban sinh vao mua he')
elif thang == 7 or thang == 8 or thang == 9 :
    print ('ban sinh vao mua thu')
elif thang == 10 or thang == 11 or thang == 12 :
    print ('ban sinh vao mua dong')
else:   
    print ('ban nhap sai thang')
#bai 9

while True:
    n = int(input('nhap n :'))
    if (1<=n<=10):
        print('Bang cuu chuong',n)
        for i in range (1,11):
            print(i,'x',n,'=',i*n)
        break
    print('n phai tu 1 den 10')
# Bai 10 : Slide 36
diem_he10 = [8.4, 6.5, 7.3, 2.6, 9.0, 5.8, 6.0, 9.7, 8.1]
def chuyen_doi_diem(diem):
    if diem >= 9.0:
        return 'A+'
    elif diem >= 8.5:
        return 'A'
    elif diem >= 8.0:
        return 'B+'
    elif diem >= 7.0:
        return 'B'
    elif diem >= 6.5:
        return 'C+'
    elif diem >= 5.5:
        return 'C'
    elif diem >= 5.0:
        return 'D+'
    elif diem >= 4.0:
        return 'D'
    else:
        return 'F'

diem_chu = []
for diem in diem_he10:
    diem_chu.append(chuyen_doi_diem(diem))

dtb_he10 = sum(diem_he10) / len(diem_he10)

def chuyen_doi_he4(diem):
    if diem >= 9.0:
        return 4.0
    elif diem >= 8.5:
        return 3.7
    elif diem >= 8.0:
        return 3.5
    elif diem >= 7.0:
        return 3.0
    elif diem >= 6.5:
        return 2.5
    elif diem >= 5.5:
        return 2.0
    elif diem >= 5.0:
        return 1.5
    elif diem >= 4.0:
        return 1.0
    else:
        return 0
diem_he10 = [8.4, 6.5, 7.3, 2.6, 9.0, 5.8, 6.0, 9.7, 8.1]

def chuyen_doi_diem(diem):
    if diem >= 9.0:
        return 'A+'
    elif diem >= 8.5:
        return 'A'
    elif diem >= 8.0:
        return 'B+'
    elif diem >= 7.0:
        return 'B'
    elif diem >= 6.5:
        return 'C+'
    elif diem >= 5.5:
        return 'C'
    elif diem >= 5.0:
        return 'D+'
    elif diem >= 4.0:
        return 'D'
    else:
        return 'F'

diem_chu = []
for diem in diem_he10:
    diem_chu.append(chuyen_doi_diem(diem))
# 2. Tính điểm trung bình
# Điểm trung bình hệ 10
dtb_he10 = sum(diem_he10) / len(diem_he10)

# Hàm chuyển đổi điểm hệ 10 sang hệ 4
def chuyen_doi_he4(diem):
    if diem >= 9.0:
        return 4.0
    elif diem >= 8.5:
        return 3.7
    elif diem >= 8.0:
        return 3.5
    elif diem >= 7.0:
        return 3.0
    elif diem >= 6.5:
        return 2.5
    elif diem >= 5.5:
        return 2.0
    elif diem >= 5.0:
        return 1.5
    elif diem >= 4.0:
        return 1.0
    else:
        return 0

# Tính điểm trung bình hệ 4
diem_he4 = []
for diem in diem_he10:
    diem_he4.append(chuyen_doi_he4(diem))
dtb_he4 = sum(diem_he4) / len(diem_he4)

# In kết quả
print("Điểm hệ 10:", diem_he10)
print("Điểm chữ tương ứng:", diem_chu)
print("---------Điểm Trung Bình---------")
print("Tổng số môn học:", len(diem_he10))
print("ĐTB hệ 10:", dtb_he10)
print("ĐTB hệ 4:", dtb_he4)

# Bài 11

N = int(input("Nhập N: "))

dem_uoc = 0
if N >=1:
    for i in range(1, N + 1):
        if N % i == 0:  
            dem_uoc += 1  
else:
    print("Vui lý nhập số nguyên dương!")
if dem_uoc == 2: 
    print(f"Số {N} là số nguyên tố!")
else:
    print(f"Số {N} không phải là số nguyên tố!")
    
# Bài 12
n = int(input("Nhập vào một số nguyên dương N (N>1): "))
print("Các số nguyên tố từ 2 tới {n} là:")
for so in range(2, n + 1):
    so_uoc = 0
    for i in range(1, so + 1):
        if so % i == 0:  
            so_uoc += 1
    
    if so_uoc == 2:
        print(so, end=", ")

# Bài 13 
so_thap_phan = int(input("Nhập vào một số tự nhiên (>0): "))
gia_tri_goc = so_thap_phan
nhi_phan = ""
while so_thap_phan > 0:
    phan_du = so_thap_phan % 2
    nhi_phan = str(phan_du) + nhi_phan
    so_thap_phan = so_thap_phan // 2

print(f"{gia_tri_goc} (hệ 10) = {nhi_phan} (hệ 2)")
#Bài 14
chieucao = [1.65, 1.7, 1.55, 1.64, 1.78, 1.67, 1.59, 1.62, 1.45, 1.8, 1.69, 1.5]
max = max(chieucao)
min = min(chieucao)

tb = sum(chieucao) / len(chieucao)

tren_tb = sum(1 for x in chieucao if x >= tb)

print("Tổng số sinh viên trong lớp: " ,len(chieucao))
print(f"Chiều cao của các sinh viên là: {chieucao}")
print(f"Sinh viên cao nhất: {max} (m)")
print(f"Sinh viên thấp nhất: {min} (m)")
print(f"Chiều cao trung bình của sinh viên: {tb} (m)")
print(f"Số sinh viên trong lớp có chiều cao >= chiều cao trung bình là: {tren_tb}")
#a