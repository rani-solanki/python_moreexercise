# i=0
# while(i<=10):
#   j=0
#   print(j)
#   j=j+1
#   i=i+1
#     from random import randint
#     num_acc = 0
#     num_rand = 0
#     acc = 0
#     while (true):
#         x = randint(0, 10)
#         num_rand += 1
#         if acc + x > 63:
#            print(' Discarding: ', x)
#            continue
#         else:
#            print('Considering: ', x)
#            num_acc += 1
#            acc += x
#            if acc == 63:
#               break
#     print('%s numbers were generated, but only %s numbers were considered to reach the %s threshold' % (num_rand, num_acc, acc))
    
#     for t in range(0,10):
#     if(t == 9): t= 0 # will this set t to 0 and launch infinite loop? No!
#     print(t)
# course_is_clear=0
# while (course_is_clear<2):
#    print("do_the_course()")
# print("next_course()")
# count = 0
# while (count < 5): count += 1; print("Hello Geek")

# done = False
# while not done: 
#     done = 4
#     print(done)
#     if done:
#         continue
#     # other stuff ... 
# importing "random" for random operations 
import random 
  
# # Initializing list  
# li = [1, 4, 5, 10, 2] 
  
# # Printing list before shuffling 
# print ("The list before shuffling is : ", end="") 
# for i in range(0, len(li)): 
#     print (li[i], end=" ") 
# print("\r") 
# # using shuffle() to shuffle the list 
# random.shuffle(li)x = True
y = 2
x = 7
print(x and y)
print(x or y)
print(not x)