a = 311
rem = 0
sum = 0
while (a != 0):
    rem = a % 10
    sum = sum+rem
    a = int(a / 10)
print("The sum of digits is: ", int(sum))