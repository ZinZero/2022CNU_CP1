k = []

while True:
    n = int(input())
    if n == 0:
        k.append(n)
        break
    else:
        k.append(n)

index = int(input())
num = int(input())

if index > len(k):
    print("Not in range")
elif index < 0:
    print("Not in range")
else:
    for i in range(0, index + 1):
        if k[i] > num:
            print(k[i])
