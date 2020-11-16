def isbeautifulstring(inputstring):
    i=0
    count1=0
    count2=0
    while(i<len(inputstring)):
        if(inputstring[i]=="a"):
            count1=count1+1
        elif(inputstring[i]=="b"):
            count2=count2+1
        i=i+1
    if(count1==count2):
        return True
    else:
        return False
user="ahdijduab"
print(isbeautifulstring(user))
