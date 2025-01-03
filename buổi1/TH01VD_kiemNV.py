#slide20_21
print("hello")
name=input("moi ban nhap ten :")
print("xin chao :",name)
#thuchanh1.1(slide23)
a = 0
A = 0
for i in range(1,6):
    print(i)
    a = a + i
    print('Gia tri cua a = ',a)
    print('----------',a)
for i in range (1,6,2):
    print (i)
    A = A + i
print('Gia tri cua A = ', A)
#thuchanh1.2(slide24)
num_a = int(so_a = input("moi nhap a:"))
num_a = int(so_b = input("moi nhap b:"))
print("a + b =",so_a + so_b)
print("a - b =",so_a - so_b)
print("a * b =",so_a * so_b)
print("a / b =",so_a / so_b)
#sile 38
6 + 7
13 + 9
a = 6
b = 7
c = 9
d = a + b + c
print (d)
# silde 46
a = 8 
b = 5
tog = a + b
hieu = a - b
tich = a * b
thuong = a / b
thuong_nguyen = a // b
thuong_du = a % b
mu = a**b
#slide  47
x = 1985
y = 3.1415926535
z = 'DONG A'
n = 15, 7, 9, 81
b = True
print( 'Kiểu dữ liệu biến x:', type(x))
print( 'Kiểu dữ liệu biến y:', type(y))
print( 'Kiếu dữ liệu biến z:', type(z))
print( 'Kiểu dữ liệu biến n:', type(n))
print( 'Kiểu dữ liệu biến b:', type (b))
# slide 52
st = 'EAUT là Trường đại học hàng đầu tại Việt Nam'
x = 'EAUT' in st
y = 'Python' in st
   #Trả về True nếu có trong chuỗi st
   #Trả về False nếu không có trong chuỗi st 
print( 'Kết quả kiểm tra EAUT:',x )
print( 'Kết quả kiểm tra Python:',y )
   #slide 62
   # Tạo một danh sách các tên học sinh
hoc_sinh = ["Lê Thùy Dung", "Trần Đức Hùng", "Nguyễn Lan Anh", "Mai Phương Thủy"]
print(hoc_sinh)  # In ra danh sách: ['Lê Thùy Dung', 'Trần Đức Hùng', 'Nguyễn Lan Anh', 'Mai Phương Thủy']

   # Tạo một danh sách các điểm số (dưới dạng chữ cái)
diem = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
print(diem)  # In ra danh sách: ['A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']

   # Tạo một danh sách các số nguyên
list_so = [9, 5, 8, 13, 0, 4, 7, 9, 11]
print(list_so)  # In ra danh sách: [9, 5, 8, 13, 0, 4, 7, 9, 11]

   # Tạo một danh sách chứa nhiều kiểu dữ liệu khác nhau (ví dụ: thông tin về một người)
person_info = ["Mary", 1998, "Tokyo, Japan", 1.70, 65]
print(person_info)  # In ra danh sách: ['Mary', 1998, 'Tokyo, Japan', 1.70, 65]

   # Tạo một danh sách rỗng
list_rong = []
print(list_rong)  # In ra danh sách rỗng: []
# slide 63
    # Truy xuất dữ liệu trong danh sách:
print("Học sinh vị trí thứ 3:", hoc_sinh[2])  # In ra tên học sinh thứ 3

    # Hiển thị tên người và chiều cao trong biến person_info
print("Họ tên:", person_info[0], "-- Chiều cao:", person_info[3])

    # Truy xuất nhiều phần tử trong danh sách
print(list_so[3:8])  # In ra các phần tử từ vị trí thứ 3 đến 7 trong danh sách list_so
# slide 65
list_a = [8,4,8,2]
list_b = [3,0,7,6,5]
list_ab = list_a + list_b
print('List moi:' , list_ab)
print(list_ab , 'co so phan tu la ' , len(list_ab))
# slide 66
    # In ra danh sách list_ab (giả sử danh sách này đã được định nghĩa trước đó)
print(list_ab)

    # Kiểm tra xem số 0 có nằm trong danh sách list_ab hay không
bol_0 = 0 in list_ab
print("Phần tử 0 có thuộc list_ab?", bol_0)

    # Kiểm tra xem số 9 có nằm trong danh sách list_ab hay không
bol_9 = 9 in list_ab
print("Phần tử 9 có thuộc list_ab ?", bol_9)
#slide 67 
print('danh sach ban dau : \n',list_ab)

list_ab.append(10)
print('danh sach them vao cuoi : \n',list_ab)

list_ab.insert(1, 100)
print('danh sach them vao vi tri t2: \n',list_ab)
#slide 69
print('ban dau : \n',list_ab)

list_ab.pop()
print('xoa cuoi \n',list_ab)

del list_ab[1]
print('xoa ptu t2 \n',list_ab)

list_ab.remove(0)
print('xoa so 0 dau tien \n',list_ab)
#slide 70
print('ban dau \n',list_ab)

print("Số 8 xuất hiện:", list_ab.count(8))

print("Số 1 xuất hiện:", list_ab.count(1))

#slide 71
      #so,chuoi
a = 10
b = a
b = 5
print('Giá trị của biến a:', a)
print('Giá trị của biến b:', b)
      #danhsach 
ds_a = [4, 5, 8, 9]
ds_b = ds_a
ds_b[1] = 10
print('Biến ds_a:', ds_a)
print('Biến ds_b:', ds_b)
#slide 72
ds_a = [4, 5, 8, 9]
ds_b = ds_a.copy()
ds_b[1] = 10
print('Biến ds_a:', ds_a)
print('Biến ds_b:', ds_b)
#slide 73
x = True
y = False
z = 5 > 8
w = 12 == 12

print('Kiểu dữ liệu của biến x:', type(x), ', Giá trị: ', x)
print('Kiểu dữ liệu của biến y:', type(y), ', Giá trị: ', y)
print('Kiểu dữ liệu của biến z:', type(z), ', Giá trị: ', z)
print('Kiểu dữ liệu của biến w:', type(w), ', Giá trị: ', w)