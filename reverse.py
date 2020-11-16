user = input("enter the number:")
li=list(user)
print(li)
i=1
lp=[]
while(i<=len(li)):
    lp.append(li[-i])
    i=i+1
# print(lp)
if(li==lp):
    print("yes")
else:
    print("no")