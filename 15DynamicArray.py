import numpy as np
#Method1
print("METHOD1")
size=int(input("Enter the size of the array: "))
my_list = list(range(size))
print("Before",my_list)
for i in range(len(my_list)):
    num= int(input("enter the element at {}: ".format(i)))
    my_list[i]=num
print("After ", my_list)

#Method2
print("METHOD2")
my_list1=[]
print("Before",my_list1)
size=int(input("Enter the size of the array: "))
for i in range(size):
    num = int(input("enter the element at {}: ".format(i)))
    my_list1.append(num)
print("After ", my_list1)

#Method3
print("METHOD3")
a = np.array([])
print("Before",a)
size=int(input("Enter the size of the array: "))
for i in range(size):
    num = int(input("enter the element at {}: ".format(i)))
    a = np.append(a, np.array([num]))
print("After ", a)
