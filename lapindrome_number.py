user="rani"
list1=list(user)
m=len(list1)/2
n=int(m)
a=[]
b=[]
i=1
while(i<n):
    a.append(list1[i])
    i=i+1
j=1
while(j<n):
    b.append(list1[-j])
    j=j+1
k=0
h=0
while(k<len(a)):
    if(a[k] in b):
        h="yes"
    else:
        break
    # print("no")
    k=k+1
print("no")
print(h)
