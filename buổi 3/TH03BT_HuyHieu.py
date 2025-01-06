#bai1 : Viết hàm greeting(): Trả về câu chào với tham số truyền vào là chuỗi họ tên và năm sinh
def greeting():
    a = str(input('nhap ten :'))
    b = int(input('nhap tuoi :'))
    print('xin chao', a.upper(), 'ban', 'sinh nam', b)
greeting()

#bai2 : Viết hàm rabbit_count(): tính số thỏ trong rừng khi truyền vào số tháng
def rabbit_count():
    x = int(input('so thang :'))
    print('trong rung co :', 2**x, 'con tho')
rabbit_count()

#bai3: Viết hàm count_mark(): trả về số sinh viên học lại và tổng số sinh viên trong lớp với tham số truyền vào là một danh sách bảng điểm
 
#Bài 4: Viết hàm bmi_show(): Trả về nhận xét dựa vào chỉ số BMI đã tính với 2 tham số truyền vào là chiều cao, cân nặng
#Bài 5: Viết hàm cal_point(): Trả về điểm trung bình hệ 10 và hệ 4 của một học sinh khi truyền vào danh sách điểm
#Bài 6: Viết hàm list_prime(): trả danh sách các số nguyên tố trong khoảng tử 1 đến n với tham số truyền vào là n