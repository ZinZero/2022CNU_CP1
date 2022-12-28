import random

x = int(input("입력해주세요 : "))

Number = []

for i in range(x+1):
    ren = random.randrange(1, x + 1)
    while ren in Number:
        ren = random.randrange(1, x+1)
    Number.append(ren)

    if int(len(Number)) == x:
        break

print(Number)