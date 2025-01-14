#Yêu cầu 1: Sử dụng dữ liệu bảng điểm của lớp 2A. Cho biết: 
            #1. ĐTB của từng học sinh trong lớp. 
            #2. Học sinh có điểm TB cao nhất. 
            #3. Học sinh có điểm trung bình thấp nhất

# Đọc dữ liệu từ file Diem_2A.txt
students = []
with open('C:\\Users\\zhieu\\OneDrive\\Documents\\Diem_2A.txt', 'r', encoding='utf-8') as file:
    for idx, line in enumerate(file):
        # Tách điểm bằng tab (\t) và chuyển sang kiểu float
        scores = list(map(float, line.strip().split('\t')))
        # Tạo tên học sinh tự động
        student_name = f"Học sinh {idx + 1}"
        # Thêm vào danh sách học sinh
        students.append({'name': student_name, 'scores': scores})

# Kiểm tra dữ liệu đã đọc
print("Dữ liệu bảng điểm đã đọc:")
for student in students:
    print(f"{student['name']}: {student['scores']}")


#  Tính điểm trung bình của từng học sinh
for student in students:
    student['average'] = sum(student['scores']) / len(student['scores'])

# In điểm trung bình của từng học sinh
print("\nĐiểm trung bình của từng học sinh:")
for student in students:
    print(f"{student['name']}: {student['average']:.2f}")

#  Tìm học sinh có điểm trung bình cao nhất
highest_avg_student = max(students, key=lambda x: x['average'])
print("\nHọc sinh có điểm trung bình cao nhất:")
print(f"{highest_avg_student['name']}: {highest_avg_student['average']:.2f}")

#  Tìm học sinh có điểm trung bình thấp nhất
lowest_avg_student = min(students, key=lambda x: x['average'])
print("\nHọc sinh có điểm trung bình thấp nhất:")
print(f"{lowest_avg_student['name']}: {lowest_avg_student['average']:.2f}")
print('---------------------------------------------------------------------------------------------------------------------------------------------')
#------------------------------------------------------------------------------------------------------------------------------------------------------
#Yêu cầu 2: Sử dụng dữ liệu bảng điểm của lớp 2A. Cho biết: 
        #1. ĐTB của từng môn học. 
        #2. Môn học có điểm TB cao nhất. 
        #3. Môn học có điểm trung bình thấp nhất
with open('C:\\Users\\zhieu\\OneDrive\\Documents\\Diem_2A.txt', 'r') as file:
    # Đọc tất cả dòng trong file và tách thành danh sách các dòng
    lines = file.readlines()

# Xử lý dữ liệu
data = []
for line in lines:
    # Tách các giá trị trong mỗi dòng và chuyển thành số
    scores = list(map(int, line.split()))
    data.append(scores)

# 1. Tính điểm trung bình (ĐTB) của từng môn học
num_subjects = len(data[0])  # Số lượng môn học (số cột)
avg_scores_per_subject = []

for i in range(num_subjects):
    total_score = 0
    for j in range(len(data)):
        total_score += data[j][i]
    avg_score = total_score / len(data)
    avg_scores_per_subject.append(avg_score)

# 2. Môn học có điểm trung bình cao nhất
max_avg_score = max(avg_scores_per_subject)
max_avg_subject = avg_scores_per_subject.index(max_avg_score) + 1  # Thêm 1 vì chỉ số môn học bắt đầu từ 1

# 3. Môn học có điểm trung bình thấp nhất
min_avg_score = min(avg_scores_per_subject)
min_avg_subject = avg_scores_per_subject.index(min_avg_score) + 1  # Thêm 1 vì chỉ số môn học bắt đầu từ 1

# In kết quả
print("ĐTB của từng môn học:")
for i, avg_score in enumerate(avg_scores_per_subject, start=1):
    print(f"Môn học {i}: {avg_score:.2f}")

print(f"\nMôn học có điểm trung bình cao nhất là môn {max_avg_subject} với điểm TB {max_avg_score:.2f}")
print(f"Môn học có điểm trung bình thấp nhất là môn {min_avg_subject} với điểm TB {min_avg_score:.2f}")

print('---------------------------------------------------------------------------------------------------------------------------------------------')
#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Yêu cầu 3: Sử dụng dữ liệu bảng điểm của lớp 2A. Cho biết: 
        #1. Sinh viên có điểm đồng đều nhất tất cả các môn. Sinh viên có điểm các môn 
        #lệch nhất trong lớp. 
        #2. Môn học có điểm đồng đều nhất. Môn học có điểm chênh lệch nhất.

import math

# Đọc dữ liệu từ file
with open('C:\\Users\\zhieu\\OneDrive\\Documents\\Diem_2A.txt', 'r') as file:
    lines = file.readlines()

# Xử lý dữ liệu
data = []
for line in lines:
    scores = list(map(int, line.split()))
    data.append(scores)

# 1. Tính độ lệch chuẩn của điểm các sinh viên
def calculate_std(scores):
    mean = sum(scores) / len(scores)
    variance = sum((score - mean) ** 2 for score in scores) / len(scores)
    return math.sqrt(variance)

# Tính độ lệch chuẩn cho từng sinh viên
std_per_student = []
for student_scores in data:
    std_per_student.append(calculate_std(student_scores))

# 2. Tính độ lệch chuẩn của điểm từng môn học
std_per_subject = []
num_subjects = len(data[0])

for i in range(num_subjects):
    subject_scores = [data[j][i] for j in range(len(data))]
    std_per_subject.append(calculate_std(subject_scores))

# 3. Sinh viên có điểm đồng đều nhất (độ lệch chuẩn thấp nhất)
min_std_student = std_per_student.index(min(std_per_student)) + 1  # Thêm 1 vì chỉ số sinh viên bắt đầu từ 1
min_std_student_scores = data[min_std_student - 1]  # Lấy điểm của sinh viên đó

# 4. Sinh viên có điểm lệch nhất (độ lệch chuẩn cao nhất)
max_std_student = std_per_student.index(max(std_per_student)) + 1  # Thêm 1 vì chỉ số sinh viên bắt đầu từ 1
max_std_student_scores = data[max_std_student - 1]  # Lấy điểm của sinh viên đó

# 5. Môn học có điểm đồng đều nhất (độ lệch chuẩn thấp nhất)
min_std_subject = std_per_subject.index(min(std_per_subject)) + 1  # Thêm 1 vì chỉ số môn học bắt đầu từ 1
min_std_subject_scores = [data[j][min_std_subject - 1] for j in range(len(data))]  # Lấy điểm của tất cả học sinh môn đó

# 6. Môn học có điểm lệch nhất (độ lệch chuẩn cao nhất)
max_std_subject = std_per_subject.index(max(std_per_subject)) + 1  # Thêm 1 vì chỉ số môn học bắt đầu từ 1
max_std_subject_scores = [data[j][max_std_subject - 1] for j in range(len(data))]  # Lấy điểm của tất cả học sinh môn đó

# In kết quả dưới dạng mảng
print(f"Sinh viên có điểm đồng đều nhất là sinh viên {min_std_student} với điểm các môn: {min_std_student_scores}")
print(f"Sinh viên có điểm lệch nhất là sinh viên {max_std_student} với điểm các môn: {max_std_student_scores}")

print(f"\nMôn học có điểm đồng đều nhất là môn {min_std_subject} với điểm của các sinh viên: {min_std_subject_scores}")
print(f"Môn học có điểm lệch nhất là môn {max_std_subject} với điểm của các sinh viên: {max_std_subject_scores}")

