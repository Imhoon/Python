a,b,c = input().split()

def median(x):
    sorted(x)
    if len(x)%2 == 0:
        return x[len(x)//2]
    else:
        return x[len(x)//2+1]

test = [[2,5,3], [4,6,4]]
for t in test:
    print(median(t))