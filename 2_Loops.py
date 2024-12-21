#while loops

x=0
while x < 5:
  print(x)
  x += 1


#For loops
names = ['John', 'Sarah', 'Kesta', 'Duncan']

for x in names:
  print(x)


##Nested loops
names = ['John', 'Sarah', 'Kesta', 'Duncan'], ['Rita', 'Conny']

for x in names:
  print(x)
  for i in x:
    print(i)

for x in range(5):
  print(x)

for x in range(5, 0, -1):
  print(x)


##using break
### ends a loop
num  = [1, 2, 4, 6, 7, 10, 11]
for x in num:
  if x == 10:
    break
  print(x)

## using continue
### skips a particular value
for x in range(1,6):
  if x==3:
    continue
  print(x)

## using pass
### empty loops
for x in range(5):
  pass