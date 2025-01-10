#slide 13
import numpy as np
      #mang 1 chieu 
a = np.array([1,2,3])
print(a)
print('loai du lieu cua bien a:',type(a))
print('kieu du lieu cua phan tu trong mang a:', a.dtype)
print('kich thuoc cua mang a:', a.shape)
print('so phan tu cua mang a:', a.size)
print(' so chieu cua mang a:', a.ndim)
#slide 14
      #mang 2 chieu
import numpy as np
b = np.array([(1,2,3),(4,5,6)])
print(b)
print('loai du lieu cua bien b:',type(b))
print('kieu du lieu cua phan tu trong mang b:', b.dtype)
print('kich thuoc cua mang b:', b.shape)
print('so phan tu cua mang b:', b.size)
print(' so chieu cua mang b:', b.ndim)
#slide 15
      #mang 3 chieu 3D
import numpy as np
c = np.array([[(1,2,3),(4,5,6)],
             [(7,8,9),(10,11,12)],
             [(13,14,15),(16,17,18)]])
print(c)
print('phan tu dau tien cua mang c:', c[0,0,0])
print('kieu du lieu cua phan tu trong mang c:', c.dtype)
print('kich thuoc cua mang c:', c.shape)
print('so phan tu cua mang c:', c.size)
print(' so chieu cua mang c:', c.ndim)
#slide 18
import numpy as np
array_zeros = np.zeros((5,3))
print(array_zeros)
print('kieu du lieu cua mang:',array_zeros.dtype) #zeros = 0
print('kich thuoc cua mag:' , array_zeros.shape)
print('so phan tu cua mang:', array_zeros.size)
print('so chieu cua mang:', array_zeros.ndim)

array_one = np.ones((3,5),dtype=np.int64) #ones = 1
print(array_one)
print('kieu du lieu cua mang:',array_one.dtype)
print('kich thuoc cua mag:' , array_one.shape)
print('so phan tu cua mang:', array_one.size)
print('so chieu cua mang:', array_one.ndim)
#slide 19
import numpy as np
array_eye = np.eye(5)
print(array_eye)
print('kieu du lieu :' , array_eye.dtype)
print('kich thuoc cua mang:', array_eye.shape)
print('so phan tu cua mang:', array_eye.size)
print('so chieu cua mang:', array_eye.ndim)
#slide 20
import numpy as np
array_random = np.random.random((3,5))
print(array_random)
print('kieu du lieu cua mang:',array_random.dtype)
print('kich thuoc cua mang:' , array_random.shape)
print('so phan tu cua mang:', array_random.size)
print('so chieu cua mang:', array_random.ndim)
#slide 21
import numpy as np
array_random = np.random.randint(low = 10,high=30,size = (2,4), dtype=np.int16)
print(array_random)
vetor_random = np.random.randint(low = 10,high=30,size = 3, dtype=np.int16)
print(vetor_random)
print('kieu du lieu cua mang:',array_random.dtype)
print('kich thuoc cua mang:' , array_random.shape)
print('so phan tu cua mang:', array_random.size)
print('so chieu cua mang:', array_random.ndim)
#slide 22
     #phuong thuc arange(a,b,steps)
     # a= start 
     # b = stop
     # steps = khoang cach
d = np.arange(1,15,2)
print('vetor d:',d)
print('so phan tu cua vetor d:',d.size)
print('----------------------------')
     #phuong thuc linspace(a,b,n)
     # a = start
     # b = stop
     # n = so phan tu
f = np.linspace(1,10,5)
print('vetor f:',f) 
print('so phan tu cua vetor f:',f.size)
#slide 25
import numpy as np
path ='data.txt'
diem_2a = np.loadtxt(path,delimiter=',',dtype=np.int16)
print(diem_2a)
print('kieu du lieu cua mang:', diem_2a.dtype)
print('kich thuoc cua mang:' , diem_2a.shape)
print('so phan tu cua mang:', diem_2a.size)
print('so chieu cua mang:', diem_2a.ndim)
#slide 28
a_float = np.array([0,15,11])
print(a_float)
print('kieu du lieu cua mang:', a_float.dtype)
print('-------------------------------')
        #chuyen tu kieu float sang int
a_int = a_float.astype(np.int16)#chuyen tu float sang int
print(a_int)
print('kieu du lieu cua mang:', a_int.dtype)
        #chuyen tu kieu int sang str
a_str = a_int.astype(np.str)
print(a_str)
print('kieu du lieu cua mang:', a_str.dtype)
print('-------------------------------')
        #chuyen tu float sang boolean
a_bol = a_float.astype(bool)
print(a_bol)
print('kieu du lieu cua mang:', a_bol.dtype)
#slide 31
a=np.array([1,2,3,4,5,6,7,8,9,10])
print('cac phan tu cua vetor a:',a)
print('------------------------------')
print('phan tu dau tien cua vetor a:',a[0])
print('phan tu cuoi cua vetor a:',a[-1])
print('phan tu thu 3 cua vetor a:',a[2])

       #truy cap toi nhieu phan tu cua vetor: a[index1:index2]
print('cac phan tu cua vetor a:',a)
print('------------------------------')
print('3 phan tu dau tien cua vetor a:',a[:3])
print('tu phan tu thu 5 toi het ', a[5:])
print('tu phan tu thu 2 den ptu t6', a[2:6])
#slide 32
     #truy cap toi 1 phan tu cua ma tran (2D) :a[index_row,index_column]
print('diem mon hoc dau tien , cua hoc sinh dau tien:',diem_2a[0,0])
print('diem mon hoc cuoi cung , cua hoc sinh cuoi cung:',diem_2a[-1,-1])
print('diem mon hon t1 cua hs t3', diem_2a[1,3])
print('-------------------------------------')
print('bang diem lop 2A' , diem_2a)
#slide 33
diem_hs5 = diem_2a[:,5]
print('diem cac mon hoc cua hoc sinh thu 5',diem_hs5)
diem_mon = diem_2a[-1,:]
print('diem cac mon hoc cuoi cung cua tat ca hoc sinh:',diem_mon)
diem_hs10 = diem_2a[:5,:10]
print('bang diem 5 mon hoc dau tien cua 10 hoc sinh dau cua lop:',diem_hs10)

