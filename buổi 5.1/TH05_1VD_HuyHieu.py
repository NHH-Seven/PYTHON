#slide 5
import numpy as np
vector_a = np.array([1,2,3,4,5,6,7,8,9,10,11,12] , dtype= np.int16)
print(vector_a)
print('so phan tu cua vetor_a:',vector_a.size)
print('------------------------------------')
       #chuyen doi vetor thanh mang 2 chieu ( n x m)
       #matrix.size = vetor.size
matrix_a = vector_a.reshape((3,4))
print('reshape ve matrix : 3 x 4')
print(matrix_a)
print('so phan tu cua matrix_a:',matrix_a.size)
print('------------------------------')
print('reshape ve matrix : 2 x 6')
matrix_b = vector_a.reshape(2,6)
print(matrix_b)
print('so phan tu cua matrix_b:',matrix_b.size)

#slide 7
a1_2d = np.array([(1,2,3,4),(5,6,7,8,),(9,10,11,12)])
print('matrix: \n',a1_2d)
print('---------------------------')
print(a1_2d.ravel())
print('\n b) ravel by column (order=\'C\')')
print(a1_2d.ravel(order='C'))
print('\n c) ravel by row (order=\'F\')')
print(a1_2d.ravel(order='F'))
#slide 9
x = np.arange(0,6)
print(x)
x1 , x2 = np.split(x,2)
print(x1 , x2)

y = np.arange(1,10)
print(y)
y1 , y2 , y3 = np.split(y,[2,6])
print(y1,y2,y3)
#slide 11 : lat ma tran
A = np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12),(13,14,15,16)])
print('ma tran A : \n',A)
a2 = np.flip(A,0)
a2 = np.flip(A)
print('lat ma tran theo hang : \n',a2)

a1 = np.flip(A,1)
a1 = np.flip(A)
print('lat ma tran theo cot : \n',a1)

#slide 16
x = np.array(8)
print('x = ',x)
print('-----------------------------------')
print('x+5 = ',x+5)
print('x-5 = ',x-5)
print('x*2 = ',x*2)
print('x/2 = ',x/2)
print('-x = ',-x)
print('x//2 = ',x//2)
print('x % 2 = ',x%2)
print('x^3 = ',x**3)
       #su dung cac phuong thuc cua numpy
print('x + 5 = ',np.add(x,5))
print('x - 5 = ',np.subtract(x,5))
print('x * 2 = ',np.multiply(x,2))
print('x / 2 = ',np.divide(x,2))
print('-x = ',np.negative(x))
print('x % 2 = ',np.mod(x,2))
print('x // 2 = ',np.floor_divide(x,2))
print('x ** 3 = ',np.power(x,3))
#slide 17
x = np.array([1,2,3,4,5,6,7,8,9,10])
print('x = ',x)
print('-----------------------------------')
print(np.abs(x))
print(np.absolute(x))

theta = np.linsapce(0, np.pi, 3)
print('theta =',theta)
print('-----------------------------------')
print('sin(theta) = ',np.sin(theta))
print('cos(theta) = ',np.cos(theta))
print('tan(theta) = ',np.tan(theta))
print('arcsin(theta) = ',np.arcsin(theta))
#slide 19
x = np.array([1,2,3])
print('x = ',x)
print('-----------------------------------')
print('e^x = ',np.exp(x))
print('2^x = ',np.exp2(x))
print('3^x = ',np.power(3,x))

y = np.array([1,2,3,100])
print('y = ',y)
print('-----------------------------------')
print('ln(y) =', y)
print('log2(y) = ',np.log2(y))
print('log10(y) = ',np.log10(y))

#slide 20

arr = np.array([20.8999 , 67.89899 , 54.43409])
print('arr = ',arr)
print('-----------------------------------')
print('around(arr) = ',np.around(arr,1))
print('around(arr) = ',np.around(arr,2))
print('ceil(arr) = ',np.ceil(arr))
print('floor(arr) = ',np.floor(arr))
#slide 23
a = np.random.randint(1,33,15)
print('vector ban dau :\n',a)
print('-----------------------------------')
a_sort = np.sort(a)
b_sort = np.flip(a_sort)
b_sort = -np.sort(-a)
print('vetoc dc sap xep theo chuoi tang dan :\n',a_sort)    
print('vetoc dc sap xep theo chuoi giam dan :\n',b_sort)
#slide 25
a_sort1 = np.sort(A,axis=0)
print('ma tran 1:\n',a_sort1)

a_sort2 = np.sort(A,axis=1)
print('ma tran 2:\n',a_sort2)

v_sort = np.sort(A,axis=None)
print('vetor :\n',v_sort)

a_sort3 = np.sort(A , axis=None).reshape(A.shape[0],A.shape[1])
print('ma tran 3:\n',a_sort3)
#slide 28
x = np.array([1,2,3,4,5,6,7,8,9,10])
t1 = np.where(x==1)
print(t1)
print('1. so phan tu thoa man dieu kien =1 ',t1[0].size)

t2 = np.where(x>10)
print(t2)
print('2. so phan tu thoa man dieu kien >10 ',t2[0].size)

t3 = np.where((x>=5)&(x<10))
print(t3)
print('3. so phan tu thoa man dieu kien >=5 & <10 ',t3[0].size)
#slide 29
arr = np.array([1,2,3,4,5,6,7],[8,9,10,11,12,13,14])
x = np.where('ma tran a : \n',arr)
print(x)
print(' so phan tu thoa man dieu kien > 4:',x[0].size)

