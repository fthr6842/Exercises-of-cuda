import cupy as cp #引入套件cupy

n = 1000
A = cp.random.rand(n, n) #在GPU上建立n by n隨機矩陣，元素存在於[0. 1]


