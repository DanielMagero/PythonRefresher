class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def checkage(self):
    if self.age < 18:
      print("Underage")
    else:
      print("Above 18")


Student1  = Student("Naomi", 33)
Student2  = Student("Jane", 17)

Student1.checkage()
Student2.checkage()

print(Student2.age,'\n',Student1.name)

Student3 = Student('','')
Student3.age  = 34
Student3.name = "Taby"

Student3.checkage()