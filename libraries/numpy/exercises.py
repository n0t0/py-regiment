#1 
import numpy as np

#2 
print(np.zeros(10))

#3 
print(np.ones(10))

#4
print(np.ones(10) * 5)

#5
print(np.arange(10,51))

#6
print(np.arange(10,51,2))

#7
mat = [[0,1,2],[3,4,5],[6,7,8]]
print(np.array(mat))
arr_2d = np.arange(9).reshape(3,3)
print(arr_2d)

#8 
print(np.eye(3))

#9 
print(np.random.rand(1))

#10 
print(np.random.randn(25))

#11
arr_2d = np.arange(0.01, 1.01, .01).reshape(10,10)
print(arr_2d)
print(np.arange(0.01, 1.01,.01).reshape(10,10))

#12
print(np.linspace(0,1,20))

#13
mat = np.arange(1,26).reshape(5,5)
print(mat[2:,1:])

#print(mat[3][-1])

#15
print(mat[:3,1:2])

#16
print(mat[-1])

#17
print(mat[-2:])

#18
print(np.sum(mat))

#19
print(np.std(mat))

#20 
print(mat)
print(mat.sum(axis=0))


