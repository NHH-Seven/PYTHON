#bai 1
N = int(input('nhap so keo :'))
M = int(input('nhap so HS :'))
if M == 0 or N == 00:
    print("Không có học sinh hoặc ko có cái kẹo nào!")
else:
    so_keo_moi_hoc_sinh = N // M
    so_keo_con_lai = N % M
    print("Mỗi học sinh được nhận:", so_keo_moi_hoc_sinh,"cai keo", "va co con lai:" , so_keo_con_lai,"cai keo")
#bai 2
name = input('nhap ten cua ban:')
ns = int(input('Nhap nam sinh : '))
print('Ban :', name.upper() ,'nam nay :' , 2024-ns , 'tuoi')
#bai 3
tho = 2
x = int(input('so thang :'))
print("trong rung co :" , tho^x,"con tho")
#bai 4
import re

doan_van = "Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890 – 1969)"

    # Đếm số ký tự
so_ky_tu = len(doan_van)
print("Số ký tự trong đoạn văn:", so_ky_tu)

    # Kiểm tra từ khóa
if "hồ chí minh" in doan_van.lower():
    print("Đoạn văn có chứa từ 'hồ chí minh'")
if "non sông" in doan_van.lower():
    print("Đoạn văn có chứa từ 'non sông'")

    # Tách đoạn văn thành các câu
cau = re.split(r'\.', doan_van)
print("Các câu trong đoạn văn:")
for cau_mot in cau:
    print(cau_mot.strip())

    # Kiểm tra ký tự đặc biệt
if re.search('[^a-zA-Z0-9\s]', doan_van):
    print("Đoạn văn có chứa ký tự đặc biệt")

    # Thay thế từ "Việt Nam"
doan_van_moi = doan_van.replace("Việt Nam", "VIỆT NAM")
print("Đoạn văn sau khi thay thế:")
print(doan_van_moi)
#bai 5
    # Khởi tạo danh sách điểm chữ của lớp
scores = ['A', 'B', 'C', 'D', 'F', 'B', 'A', 'F', 'C', 'B', 'A']

    # 1) Cho biết số sinh viên trong lớp
num_students = len(scores)
print(f"Số sinh viên trong lớp: {num_students}")

    # 2) Bao nhiêu sinh viên phải học lại môn này (diem F)
failing_students = scores.count('F')
print(f"Số sinh viên phải học lại: {failing_students}")

    # 3) Bao nhiêu sinh viên có điểm từ B trở lên
high_achievers = sum(score in ['A', 'B'] for score in scores)
print(f"Số sinh viên đạt điểm từ B trở lên: {high_achievers}")

    # 4) Loại bỏ sinh viên đầu tiên và cuối cùng trong danh sách
updated_scores = scores[1:-1]
print(f"Danh sách điểm mới: {updated_scores}")
