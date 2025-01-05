#slide 5
a = 10
b = 8

tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
thuong_nguyen = a // b
thuong_du = a % b
mu = a ** b
#slide 8
a= 10
b = 8
print('1) lon hon (a>b):', a>b)
print('2) nho hon (a<b):', a<b)
print('3) lon hon hoac bang (a>=b):', a>=b)
print('4) nho hon hoac bang (a<=b):', a<=b)
print('5) bang nhau (a==b):', a==b)
print('6) khac nhau (a!=b):', a!=b)
#slide 9
x = 15
y = True
kt = (x>3) and (x<10) 
kt2 = (x>3) or (x<10)
kt3 = not y
print('1) phep toan and:',kt)
print('2) phep toan or:',kt2)
print('3) phep toan not:',kt3)
#slide 11
so_tien = input ('nhap so tien :')
so_tien = int(so_tien)
if (so_tien > 10000000000):
    print('ban la ti phu')
else:
    print('ban la 1 thang ngheo')

#slide 12
num = 3
if num > 0 :
    print(num , 'la so duong')
print('thong diep nay luon duoc in')
num = -1
if num > 0 :
    print(num , 'la so am')
print('thong diep nay luon duoc in')
#slide 13
so = int(intput('nhap so :'))
if so % 2 == 0:
    print(so , 'la so chan')
print( 'luon hien ra thong bao nay')
#slide 14
num = 3
if num >= 0 :
    print(num , 'la so duong')
else:
    print(num , 'la so am')
num = -1
if num<=0 :
    print(num , 'la so am')
else:
    print(num , 'la so duong')
#slide 15
so = int(input('nhap so :'))
if so % 2 == 0:
    print(so , 'la so chan')
else:
    print(so , 'la so le')
#slide 17
so = int(input('nhap so :'))
if so == 0:
    print('Chao anh hieu dep trai')
elif so == 1:
    print('Chao chi xinh gai')
else:
    print('Chao GAY')
#slide 18
num = float(input('nhap so :'))
if num >= 0:
    if num == 0:
        print(num , 'la so 0')
    else:
        print(num , 'la so duong')
else:
    print(num , 'la so am')
#slide 25
n = int(input('Em sinh thang may?'))
i = 1
while i <= n:
    print(i,') I LOVE YOU!')
    i = i+1
print('-----------EAUT---------')
#slide 26
n = int(input('Em sinh thang may?'))
i = 1
while i <= n:
    print(i,') I LOVE YOU!')
    if(i==3):
        break
    i = i+1
print('-----------EAUT---------')
#slide 27
n = 20 
i = 1
while (i<=n):
    i = i+ 1
    if(i%3!=0):
        continue
    print(i)
print('-----------EAUT---------')
#slide 28
while True:
    n = int(input('Em sinh thang may?'))
    if (1<=n<= 12):
        break
    print('Vui long nhap lai')
print('chao em co gai thang',n)
#slide 29
n = 10 
tich = 1
tong = 0
for i in range(1,n+1):
    tich = tich*i
    tong = tong + i
print('10! = ',tich)
print('10+= ',tong)
#slide 30
st = 'EAUT IN MY MIND'
dem = 0
for i in st:
    if(i == 'M'): dem = dem + 1
print('So ky tu M trong chuoi la:', dem)
#slide 31
hoc_sinh = ["Lê Thùy Dung", "Trần Đức Hùng", "Nguyễn Lan Anh", "Mai Phương Thủy"]
print('danh sach hoc sinh bao gom:')
tt = 1
for i in hoc_sinh:
    print(tt,')',i)
    tt = tt + 1
#slide 33
for i in range(5):
    print('i = ',i)
for i in range(5,10):
    print('i=',i)
for i in range(2,11,2):
    print('i=', i)
#slide 34
for i in range(2,10):
    print('bang cua chuong ', i)
    for j in range(1,11):
        print(i , 'x', j , '= ', i*j)
    print('-----------')
