##list indexing
num  = [1, 2, 4, 6, 7, 10, 11]

print(num[1])
print(num[-1])

##range
print(num[2:4])
print(num[:4])
print(num[4:])

## inserting by index
num[3] = 88
print(num)

num.append(77)
print(num)

num.insert(6, 55)
print(num)

num.remove(4)
print(num)

num.pop(4)
print(num)

num.pop()
print(num)

del num[2]
print(num)

del num

num  = [1, 2, 4, 6, 7, 10, 11]
num.clear()
print(num)

num  = [22, 34, 1, 2, 4, 6, 7, 10, 11]
num.sort()
print(num)

num2  = [i for i in range(3, 20)]
print(num2)