a = int(input())

Number = []

def prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if (x % i) == 0:
            return False
    return True

for i in range(a+1):
    if prime(i):
        Number.append(a)

print(len(Number))
