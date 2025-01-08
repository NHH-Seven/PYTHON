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
def count_mark():
    scores = input("Nhập danh sách điểm (cách nhau bởi dấu phẩy): ")
    scores = [float(score.strip()) for score in scores.split(",")]
    total_students = len(scores)
    failed_students = len([score for score in scores if score < 5])
    return f"Số sinh viên học lại: {failed_students}, Tổng số sinh viên: {total_students}"

print(count_mark())
#Bài 4: Viết hàm bmi_show(): Trả về nhận xét dựa vào chỉ số BMI đã tính với 2 tham số truyền vào là chiều cao, cân nặng
def bmi_show(height, weight):
    BMI = weight / (height * height)
    if BMI < 18.5:
        ketqua = "Gầy"
    elif BMI > 18.5 and BMI < 24.9:
        ketqua = "Bình thường"
    elif BMI > 25 and BMI < 29.9:
        ketqua = "Thừa cân"
    else:
        ketqua = "Béo phì"
    return f"BMI: {BMI:.2f}. Nhận xét: {ketqua}"
height = float(input("Nhập chieu cao: "))
weight = float(input("Nhập cân nặng: "))
print(bmi_show(height, weight))

#Bài 5: Viết hàm cal_point(): Trả về điểm trung bình hệ 10 và hệ 4 của một học sinh khi truyền vào danh sách điểm
def cal_point():
    scores = list(map(float, input("Nhập danh sách điểm (cách nhau bởi dấu cách): ").split(" ")))
    avg_10 = sum(scores) / len(scores)
    avg_4 = (avg_10 / 10) * 4
    return f"Điểm trung bình hệ 10: {avg_10:.2f}, hệ 4: {avg_4:.2f}"

print(cal_point())
#Bài 6: Viết hàm list_prime(): trả danh sách các số nguyên tố trong khoảng tử 1 đến n với tham số truyền vào là n
def list_prime():
    n = int(input("Nhập một số nguyên dương n: "))
    if n < 2:
        return "Không có số nguyên tố nào trong khoảng từ 1 đến n!"

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_numbers = [num for num in range(2, n + 1) if is_prime(num)]
    return f"Các số nguyên tố từ 1 đến {n} là: {prime_numbers}"

print(list_prime())
