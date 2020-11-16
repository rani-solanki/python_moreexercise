question_list = ["what is your name","which is type your school","what are you in study"]
option_list = [["rani","rinki","komal","sonam"],["gov","private","college","ngo"],["doctor","police","mppsc","software engineering"]]
solution_list=[1,3,4]
index = 0
while(index<len(question_list)):
    print(index+1,question_list[index])
    num = 0
    while(num<len(question_list)):
        print(num+1,option_list[index][num])
        num=num+1
    user = int(input("enter the number"))
    a = int(input("enter any number bitween 1,2:"))
    if(a==solution_list[index]):
        print("congrets")
    else:
        print("wrong answere")
        break
    index = index+1
print("aap pehle hi le chuke ho")