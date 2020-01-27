import numpy as np

my_list = [1,2,3]

print(type(np.array(my_list)))
arr = np.array(my_list)

my_mat = [[1,2,3], [4,5,6], [7,8,9]]
print(np.array(my_mat))

print(np.arange(0,11,2))

print(np.zeros(3))
print(np.zeros(4))

print(np.zeros((2,3)))

print(np.ones(3))
print(np.ones((3,4)))

print(np.linspace(0,10,5))


print(np.eye(4))

print(np.random.rand(5))
print(np.random.rand(5,5))

print(np.random.randn(4))
print(np.random.randn(4,4))

print(np.random.randint(1,100, 10))


arr = np.arange(25)
ran_arr = np.random.randint(0, 50, 10)

print(arr.reshape(5,5))

print(ran_arr.max())
print(ran_arr.min())

print(ran_arr.argmax())
print(ran_arr.argmin())

print(arr.shape)
print(arr.dtype)

# from numpy.random import randint 