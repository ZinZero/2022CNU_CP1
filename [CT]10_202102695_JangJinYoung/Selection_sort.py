list1 = [5, 9, 2, 3, 1]

print(0, '번째 반복 : ', list1)
for i in range(len(list1) - 1):
    min_v = i

    for j in range(i + 1, len(list1)):
        if list1[min_v] > list1[j]:
            min_v = j

    list1[i], list1[min_v] = list1[min_v], list1[i]

    print(i + 1, '번째 반복 : ', list1)

print(list1)
