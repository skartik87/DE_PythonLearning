a=21
count=0
for i in range(1,22):
    if a%i==0:
        count+=1
if count==2:
    print("Prime Number")
else:
    print("Not a Prime Number")