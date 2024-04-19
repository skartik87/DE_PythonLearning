a=[10,20,30,400,50,60]
maxnum=0
for i in range(len(a)):
    maxnum=a[i]
    for j in range(len(a)):
        if(a[j]>maxnum):
            maxnum=a[j]
print("MAX NUMBER USING LOOP",maxnum)
print("MAX NUMBER USING FUNCTION",max(a))