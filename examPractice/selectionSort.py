list1 = [5, 9, 2, 3, 1]

print("0번째 반복 : ", list1)

for i in range(len(list1) - 1):
    minValue = min(list1[i:])
    index = list1.index(minValue)

    if list1[i] > minValue:
        list1[index] = list1[i]
        list1[i] = minValue

    print(i + 1, "번째 반복 : ", list1)

print(list1)
