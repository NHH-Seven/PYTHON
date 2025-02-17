import numpy as np
#slide 40
print ('diem cao nhat cua lop :' , diem_2a.max())
print ('diem thap nhat cua lop :' , diem_2a.min())
    #liet ke diem cao nhat voi diem thap nhat theo mon hoc
for i in range(0,diem_2a.shape[0]):
    print('Mon ',diem_2a[i].max(),
          '--diem min:', diem_2a[i].min())
for i in range(0,diem_2a.shape[1]):
    print('Hoc sinh ',diem_2a[:,i].max(),
          '--diem min:', diem_2a[:,i].min())
#slide 41
print('tong tat ca diem trung cua lop 2a:',diem_2a.sum())
print('------------------------------------')
for i in range(0,diem_2a.shape[1]):
    print('tong diem cac mon cua hoc sinh ',i,':',diem_2a[:,i].sum())
#slide 43
print('diem trung binh cua lop 2a:',diem_2a.mean()) 
print('------------------------------------')
      #tinh diem diem trung binh cac hoc sinh trong lop
      #cach 1
for i in range(0,diem_2a.shape[1]):
    print('diem trung binh cua hoc sinh ',i,':',diem_2a[:,i].mean())
      #cach 2
    mean_2a = diem_2a.mean(axis=0)
for i in range(0,diem_2a.shape[1]):
    print('diem trung binh cua hoc sinh ',i,':',mean_2a[i])
#slide 44
a = diem_2a[1,:15]
print('mang a ban dau \n',a)
print('so phan tu trong mang a:', a.size)
print('mang a da sap xep : \n',a.sort(a,))
print('gia tri trung binh mean :', np.mean(a))
print('gia tri trung binh median :', np.median(a))
#slide 45
from scipy import stats as sp
for i in range(0,diem_2a.shape[1]):
    print('Mon' , i , ':diem xuat hien nhieu nhat:', a[0],
          'so lan :', a[1])
print(type(a))
#slide 46
for i in range(0,diem_2a.shape[1]):
    print('do lech diem cua hoc sinh ',i,':',diem_2a[:,i].max()-diem_2a[:,i].min())
#slide 47
a = np.array([1,2,3,4,5,6,7,8,9,10])
print('phan tu mang a:',a)
print('Gia tri trung binh :', a.mean())
print('Do lech chuan :', a.std())
print('------------------------------------')

b = np.array([1,2,3,4,5,6,7,8,9,10])
print('phan tu mang b:',b)
print('Gia tri trung binh :', b.mean())
print('Do lech chuan :', b.std())
#slide 53
a_giohoc = np.array([1,2,3,4,5,6,7,8,9,10])
b_giohoc = np.array([1,2,3,4,5,6,7,8,9,10])
co = np.corrcoef(a_giohoc,b_giohoc)
print(type(co))
print('he so tuong quan :\n', co)

