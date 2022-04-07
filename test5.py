import random

num1 = []
num1.append(24)
num1.append(34)
num1.append(24)
num1.append(24)
num1.append(12)
print(num1)

num2 = []
num2.append(100)
num2.append(104)
num2.append(103)
num2.append(107)
print(num2)

num1.extend(num2)
print(num1)

print(num1)
print(num1.count(24))

print(num1.index(12,0,len(num1)))

num2.insert(0,999)
print(num2)

num2.remove(999)
print(num2)

num2.sort()
print(num2)