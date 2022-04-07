import random

num1 = []
num1.append(34)
num1.append(54)
num1.append(24)
num1.append(14)
print(num1)

num2 = []
num2.append(100)
num2.append(105)
num2.append(102)
num2.append(190)
print(num2)

num1.extend(num2)
print(num1)

num1.insert(1,100)
num1.insert(4,250)
print(num1)

num1.remove(250)
print(num1)

num1.sort()
print(num1) 




