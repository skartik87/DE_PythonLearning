a=0
print(str(a)+ " ",end="")
b=1
print(str(b)+ " ",end="")
for i in range(1,10):
    c = a+b
    print(str(c)+ " ",end="")
    a = b
    b = c
