#Bài 16: slide 28 : Xây dựng lớp Person
    #Xây dựng lớp Person: 
    #• Gồm 4 Thuộc tính: – họ tên (name), năm sinh (year), chiều cao (height), cân nặng (weight) – Giá trị mặc định của các thuộc tính là thông tin của bạn 
    #• Gồm 2 Phương thức: – Geeting(): Hiển thị thông tin của Person – Bmi(): Tính toán chỉ số BMI của Person
class Person:
    def __init__(self, name, year, height, weight):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight

    def get_info(self):
        return f"Name: {self.name}\nYear: {self.year}\nHeight: {self.height}\nWeight: {self.weight}"

    def bmi(self):
        BMI = self.weight / (self.height * self.height)
        return f"BMI: {BMI:.2f}"
    def kt(self):
        if self.name.isalpha():
            return "Chỉ nhập chuỗi!"
        if self.year.isdigit():
            return "Chỉ nhập số!"
        if self.height > 0 and self.weight > 0:
            return "chỉ số lớn hơn 0!"
        return True
name = str(input("Nhập họ tên: "))
year = int(input("Nhập năm sinh: "))
height = float(input("Nhập chiều cao: "))
weight = float(input("Nhập cân nặng: "))
person = Person(name, year, height, weight)
if person.kt()== True:
    print(person.get_info())
    print(person.bmi())
else:
    print(person.kt())

#Bài 17: slide 44 : Đọc/Ghi file
