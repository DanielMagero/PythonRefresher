file = open("Sample.text", 'w')

file.write("Object1 \n")
file.write("Object2 \n")
file.write("Object3 \n")

file.close()

file = open("Sample.text")
for x in file:
  print(x)

file.close()

Students = [['Name', 'Age', 'Course'], 
            ['Gabe', '21', 'BSWASA'], 
            ['Rita', '19', 'BSIT']]

print(Students[1][1])

file = open('students.txt', 'w')
rows = len(Students)
cols = len(Students[0]) #num of columns is the number of elemnents in the first list

for i in range(rows):
  for j in range(cols):
    file.write(Students[i][j] + '\n')
file.close()