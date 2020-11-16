list1 = [1,3,4,5,23]
list2 = [4,7,1,2,3]
index = 0
b = []
while(index<len(list1)):
    num = 0
    while(num<len(list2)):
        if(list1[index]==list2[num]):
            b.append(list1[index])
        num = num+1
    index=index+1
print(b)
    