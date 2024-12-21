tuple1  = ('king', 'princess', 'queen', 'prince')

print(tuple1[1])

## in order to add anything to a tuple
list1 = list(tuple1)
list1.append('duke')
tuple1 = tuple(list1)
print(tuple1)

##finding index
print(tuple1.index('duke'))