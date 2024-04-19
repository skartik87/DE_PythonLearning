a = 311
b=a
rem = 0
rev = 0
while (a != 0):
    rem = a % 10
    rev = rev*10+rem
    a = int(a / 10)
print("Reverse of "+str(b)+" is: "+str(rev))