user=[1,0,1]
i=0
a=1
sum=0
while(i<len(user)):
    sum=sum+(2**i*user[i])
    i=i+1
    a=a+1
print(sum)