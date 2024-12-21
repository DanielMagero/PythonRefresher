dict1 = {
  "Name": "King",
  "Gender": "Male",
  "Status": "Single",
}

print(dict1['Name'])

##adding new items to the dictionary
dict1['Number'] = '045778823'
dict1['Residence'] = 'Blackley'

print(dict1)

#dict.pop('Status') --doesn't work on strings

print(dict1)

##creating dictionary from user input
x = 1
dict2  = {}

while x < 4:
  id = x
  name  = input('Input name: ')
  Course = input('Input Course: ')
  dict2['id'] = id
  dict2['Name'] = name
  dict2['Course'] = Course
  print(dict2)

  x += 1