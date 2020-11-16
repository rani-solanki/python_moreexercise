list1 = [1,5,10,12,16,4]
list2 = [1,2,10,3,16,14]
index = 0
a = []
b=[]
while(index<len(list1)):
    a.append(list1[index])
    num = 0
    while(num<len(list2)):
        if(list1[index]==list2[num]):
            b.append(list2[num])
        num=num+1
    index=index+1
print(a+b)