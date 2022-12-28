x = input()

xx = x.split(" ")

Number = []
result = []

for i in range(0, len(xx)):
    Number.append(int(xx[i]))

for j in Number:
    if j not in result:
        result.append(j)
print(result)
