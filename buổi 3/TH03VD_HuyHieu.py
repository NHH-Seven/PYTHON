#slide 4
def hello_MDC(str):
    print('hi', str , ',How are you?')
    print('Have a nice day!')

hello_MDC('Huy Hieu')
#slide 6
def giai_thua(n):
    tich = 1
    for i in range(1, n+1):
        tich *= i
    return tich
n = int(input('nhap n :'))
print(n,'!=', giai_thua(n))
#slide 7
n = int(input('nhap n :'))
print(n,'!=', giai_thua(n))
print('12! = ', giai_thua(12))
#slide 8
def hello_MDC(str):
    print('hi', str , ',How are you?')
    print('Have a nice day!')
def giai_thua(n):
    tich = 1
    for i in range(1, n+1):
        tich *= i
    return tich
#slide 9
def all_ab(a,b):
    add = a+b
    sub = a-b
    multi = a*b
    div = a/b
    return add,sub,multi,div
a = 10
b = 6
tong , hieu , tich , thuong = all_ab(a,b)
print('tong = ',tong)
print('hieu = ',hieu)
print('tich = ',tich)
print('thuong = ',thuong)
#slide 10
def giai_thua(n):
    tich = 1
    for i in range(1, n+1):
        tich *= i
    return tich
print('12! = ', giai_thua(12))
         #error
print('12! = ', giai_thua())#phai truyen tham so n
#slide 12
def sum_ab(a=5,b=7):
    total = a+b
    return total
print (sum_ab(8,13))
print(sum_ab())
#slide 13
def get_sum(*num):
    tmp = 0
    for i in num:
        tmp += i
    return tmp
result = get_sum(1,2,3,4,5,6,7,8,9,10)
print ('ket qua :', result)
#slide 14
x = 300
y = 800
def myfunc():
    x = 200
    total = x + y
    print('(local) x = ', x)
    print('total : ', total)
myfunc()
print('------------')
print('(global) x = ', x)
#slide 15
x = lambda a: a + 10
print(x(5))
print(x(10))

x = lambda a, b: a * b
print(x(5, 6))
