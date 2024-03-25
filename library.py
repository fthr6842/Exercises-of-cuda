import cupy as cp #引入套件cupy

n = 1000
A = cp.random.rand(n, n) #在GPU上建立n by n隨機矩陣，元素存在於[0. 1]
b = cp.random.rand(n, 1)
F = cp.fft.fft(b) #Fourier transform
C = cp.linalg.cholesky() #
Sum = cp.add() #矩陣相加
Mul = cp.matmul() #矩陣相乘
