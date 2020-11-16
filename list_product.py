def adjacentElementsProduct(inputArray):
    i=0
    b=[]
    while(i<len(inputArray)-1):
        a=(inputArray[i]*inputArray[i+1])
        b.append(a)
        i=i+1
    return(max(b))
user=[2,-3,6,7,-2,-3]
print(adjacentElementsProduct(user))
    
