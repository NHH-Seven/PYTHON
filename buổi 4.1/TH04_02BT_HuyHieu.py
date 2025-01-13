#bai 1 :  Học viên tạo một ma trận vuông cấp n (n hàng x n cột), 
          #bao gồm các phần tử, là những số nguyên ngẫu nhiên trong khoảng 
          #(0-100) như minh họa, với n = 12
import numpy as np
n = 12
matrix = np.random.randint(0, 101, size=(n, n))
print('Ma Tran: \n',matrix)
print('Kich Thuoc: ',matrix.shape)
print('so phan tu cua ma tran : ', matrix.size)
print('so chieu cua ma tran : ', matrix.ndim)
#bai 2 :  Sử dụng ma trận tạo được trong yêu cầu 1, Học viên tạo 2 vector như sau: 
          #• v_chinh: bao gồm các phần tử nằm trên đường chéo chính của ma trận. 
          #• V_phu: bao gồm các phần tử nằm trên đường chéo phụ của ma trận
