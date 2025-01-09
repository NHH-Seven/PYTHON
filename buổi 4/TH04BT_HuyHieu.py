#Bài 16: slide 28 : Xây dựng lớp Person
    #Xây dựng lớp Person: 
    #• Gồm 4 Thuộc tính: – họ tên (name), năm sinh (year), chiều cao (height), cân nặng (weight) – Giá trị mặc định của các thuộc tính là thông tin của bạn 
    #• Gồm 2 Phương thức: – Geeting(): Hiển thị thông tin của Person – Bmi(): Tính toán chỉ số BMI của Person
from datetime import datetime

class Person:
    def __init__(self, name, year, height, weight):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight

    def greeting(self):
        """Hiển thị thông tin của Person."""
        print(f"Họ tên: {self.name}")
        print(f"Năm sinh: {self.year}")
        print(f"Chiều cao: {self.height} m")
        print(f"Cân nặng: {self.weight} kg")

    def bmi(self):
        """Tính toán chỉ số BMI."""
        bmi_value = self.weight / (self.height ** 2)
        return round(bmi_value, 2)


def get_valid_name(prompt):
    """Hàm để lấy họ tên hợp lệ."""
    while True:
        name = input(prompt).strip()
        if name and name.replace(" ", "").isalpha():
            return name
        print("Tên không hợp lệ. Vui lòng nhập lại (chỉ chứa chữ cái và không để trống).")


def get_valid_year(prompt, min_year, max_year):
    """Hàm để lấy năm sinh hợp lệ trong khoảng [min_year, max_year]."""
    while True:
        try:
            year = int(input(prompt))
            if min_year <= year <= max_year:
                return year
            else:
                print(f"Năm sinh phải trong khoảng từ {min_year} đến {max_year}.")
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập lại một số nguyên.")


def get_valid_input(prompt, value_type):
    """Hàm để lấy đầu vào hợp lệ với kiểm tra ngoại lệ."""
    while True:
        try:
            value = value_type(input(prompt))
            return value
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập lại!")


if __name__ == "__main__":
    current_year = datetime.now().year  # Lấy năm hiện tại

    # Nhập thông tin từ người dùng với kiểm tra ngoại lệ
    
    name = get_valid_name("Nhập họ tên: ")
    year = get_valid_year("Nhập năm sinh: ", 1900, current_year)
    height = get_valid_input("Nhập chiều cao (m): ", float)
    weight = get_valid_input("Nhập cân nặng (kg): ", float)

    # Tạo đối tượng Person
    person = Person(name.upper(), year, height, weight)

    # Hiển thị thông tin và tính chỉ số BMI
    print('---------------------------------')
    person.greeting()
    print(f"Chỉ số BMI: {person.bmi()}")


#Bài 17: slide 44 : Đọc/Ghi file
    #Tìm phần tử lớn nhất và nhỏ nhất trong dãy, sau đó thực hiện đổi chỗ phần tử lớn nhất 
    #xuất hiện đầu tiên trong dãy cho phần tử nhỏ nhất xuất hiện đầu tiên trong dãy. Lưu dãy 
    #mới đã đổi chỗ sang file dayso2_bai17.txt
def read_from_file(filename):
    """
    Đọc dãy số từ file và chuyển thành danh sách số nguyên.
    """
    with open(filename, "r") as file:
        data = file.read().strip()  # Đọc nội dung và xóa khoảng trắng thừa
        return list(map(int, data.split()))  # Chuyển thành danh sách số nguyên


def find_and_swap_max_min(numbers):
    """
    Tìm phần tử lớn nhất và nhỏ nhất trong dãy, sau đó đổi chỗ chúng.
    """
    if not numbers:
        return numbers  # Dãy rỗng, không xử lý
    
    max_value = max(numbers)
    min_value = min(numbers)

    # Tìm vị trí phần tử lớn nhất và nhỏ nhất đầu tiên
    max_index = numbers.index(max(numbers))
    min_index = numbers.index(min(numbers))

    print(f"Giá trị lớn nhất: {max_value}, Giá trị nhỏ nhất: {min_value}")

    
    # Đổi chỗ phần tử lớn nhất và nhỏ nhất
    numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]
    return numbers


def save_to_file(filename, data):
    """
    Lưu dãy số vào file.
    """
    with open(filename, "w") as file:
        file.write(" ".join(map(str, data)))


if __name__ == "__main__":
    input_file = "C:\\Users\\zhieu\\OneDrive\\Documents\\daysoBai17_slide44.txt"  # Đường dẫn file chứa chuỗi ban đầu
    output_file = "C:\\Users\\zhieu\\OneDrive\\Documents\\daysoBai17_slide44_2.txt"  # Đường dẫn file xuất kết quả

    # Đọc dãy số từ file
    numbers = read_from_file(input_file)
    print("Dãy ban đầu từ file:", numbers)

    # Tìm và đổi chỗ phần tử lớn nhất và nhỏ nhất
    new_numbers = find_and_swap_max_min(numbers)

    # Hiển thị dãy sau khi đổi chỗ
    print("Dãy sau khi đổi chỗ:", new_numbers)

    # Lưu kết quả vào file
    save_to_file(output_file, new_numbers)
    print(f"Kết quả đã được lưu vào file {output_file}")
