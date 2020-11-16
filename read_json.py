import json
# with open("more_exercise.json") as data_file:
plce=open("more_exercise.json","w")
# print(plce)    
data = json.load(data_file)
# print(data)

users1 = ['users']
print(users1)

for user in data:
  counter = 0
  print ("users full name is " + user['firstName'] + ' ' + user['lastName'])
  while counter < len([users]):
    print ("users mobile number is " + user['details']['mobileNo'])
    print ("users age  is " + user['details']['age'])
    print ("users city is " + user['details']['city'])