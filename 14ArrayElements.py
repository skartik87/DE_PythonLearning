import numpy as np
#LIST
arr=[1,2,3,4]
for i in range(len(arr)):
    #The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
    print(arr[i],hex(id(arr[i])))
#NUMPY
a = np.array([1,2,3,4])
for i in range(a.size):
    print(a[i],a[i].data)
    print(a[i], a[i].__array_interface__['data'])  # __array_interface__['data'] prints the address of a numpy array

