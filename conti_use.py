ci = 0
a = 'geeksforgeeks'
i=0
while i < len(a):  
    if a[i] == 'e' or a[i] == 's':  
        i += 1
        continue
    print('Current Letter :', a[i]) 
    i += 1
# how to use continue statement
i=0
while(i<10):
    if(i%2==0):
        # here it will skip the value
        continue
    print(i)
    i=i+1

