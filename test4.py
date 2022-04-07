import random as rd

num = rd.sample(range(0,100),10)
print(num)
ran = [rd.choice(num)for i in range(6)]
print(ran)

import sys
min = sys.minsize
for i in range(len(num)):
    if num[i] < min:
        min = num[i]
print(min)
