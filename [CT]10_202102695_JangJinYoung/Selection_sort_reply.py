list1 = [5, 9, 2, 3, 1]

print(0, '번째 반복 : ', list1)
for i in range(len(list1) - 1):
    min_value = min(list1[i:])
    index = list1.index(min_value)

    if list1[i] > min_value:
        list1[index] = list1[i]
        list1[i] = min_value

    print(i +1, '번째 반복 : ', list1)

print(list1)