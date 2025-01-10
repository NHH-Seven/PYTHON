#slide 21
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getarea(self):
        area = round(self.width * self.height,1)
        return area
    def getPerimeter(self):
        perimeter = round((self.width + self.height) * 2,1)
        return perimeter
#slide 26
r1 = Rectangle(10, 20)
x = r1.width 
y = r1.height
print('Chieu dai: ', x)
print('Chieu rong: ', y)
dt = r1.getarea()
cv = r1.getPerimeter()
print('Dien tich: ', dt)
print('Chu vi: ', cv)
#slide 37
f = open('input.txt')
st = f.read()
print('noi dung file:')
print(st)

f = open('input.txt','r')
st1 = f.read(15)
print(st1, '-- so ky tu la :', len(st1))
#slide 38
f = open('input.txt')
print(f.readline())
print(f.readline())

f = open('input.txt' , 'r')
for x in f:
    print(x)
f.close()
#slide 39
f1 = open('input.txt', 'w')
st = 'welcome to python'
f1.write(st)
f1.close()

#slide 40
f1 = open('input.txt', 'a')
st = '\n welcome to python'
f1.write(st)
f1.close()
f = open('input.txt', 'r')
print(f.read())
#slide 41
f2 = open('input.txt')
print('ten file:', f2.name)
print('che do mo file:', f2.mode)
print('trang thai dong file:', f2.closed)
#slide 42
  #ghi du lieu vao file data.txt
fo = open('data.txt', 'w')
fo.write('Hello world!\n')
fo.close()
print('File da duoc ghi thanh cong!')
  #doc va ghi du lieu tu 1 file
obj = open('data.txt', 'w')
obj.write('Hello world!\n')
obj.close()
obj1 = open('data.txt', 'r')
data = obj1.read()
print(data)
obj1.close()
obj2 = open('data.txt', 'r')
s1 = obj2.read(20)
print(s1)
obj2.close()

