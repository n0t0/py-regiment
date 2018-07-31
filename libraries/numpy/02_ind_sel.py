import numpy as np

arr = np.arange(0, 11)
print(arr)

print(arr[8])
print(arr[1:5])
print(arr[0:5])
print(arr[:6])
print(arr[6:])

arr[0:5] = 100
print(arr)

# numpy doesn't auto copy array due to memory issues with large arrays

arr_copy = arr.copy()
print(arr_copy)
arr_copy[:] = 100
print(arr_copy)

## Matrix 

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)

print(arr_2d[0][0])
print(arr_2d[0])

print(arr_2d[0, 1])


print(arr_2d[:2,1:])
print(arr_2d[1:,:2])

# Conditional Selection 

arr = np.arange(1,11)
print(arr)

bool_arr = arr > 5 
print(bool_arr)

print(arr[bool_arr])
print(arr[arr>5])

arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)
print(arr_2d[1:3,4:6])