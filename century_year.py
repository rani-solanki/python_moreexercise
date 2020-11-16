def century_year(year):
    if(year%100==0):
        return(int(user/100))
    elif(year%100!=0):
        return int((year+100)/100)
    else:
       return ("nothing",year)
user=int(input("enter the number"))
print(century_year(user))