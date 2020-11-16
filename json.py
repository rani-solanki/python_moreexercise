{
    "users": [{
            "firstName": "vidur",
            "lastName": "singla",
            "details": {
                "age": 21,
                "mobileNo": 1234567890,
                "City": "Delhi"
            }
        },
        {
            "firstName": "rishabh",
            "lastName": "verma",
            "details": {
                "age": 22,
                "mobileNo": 12345678320,
                "City": "Chandigarh"
            }
        },
        {
            "firstName": "abhishek",
            "lastName": "gupta",
            "details": {
                "age": 25,
                "mobileNo": 12332567890,
                "City": "Gurgaon"
            }
        }
    ]
}
#  import json
# with open('user.json') as data_file:    
#     data = json.load(data_file)
# ad(data_filedata = json.lo)
users = ['users']
for users in users:
  counter = 0
  details=['details']
  while counter < len(users[details]):
    print ("users full name is " + users['firstName'] + ' ' + users['lastName'])
#   while counter < len(user['details']):
    print ("users mobile number is " + users['details'][counter]['mobileNo'])
    print ("users age  is " + users['details'][counter]['age'])
    print ("users city is " + users['details'][counter]['city'])
