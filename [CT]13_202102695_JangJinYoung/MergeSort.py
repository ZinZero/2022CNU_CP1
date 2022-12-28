def mergesort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left)
    mergesort(right)

    x = 0
    y = 0
    z = 0

    while x < len(left) and y < len(right):
        if left[x] < right[y]:
            arr[z] = left[x]
            x += 1
            z += 1
        else:
            arr[z] = right[y]
            y += 1
            z += 1

    while x < len(left):
        arr[z] = left[x]
        z += 1
        x += 1
    while y < len(right):
        arr[z] = right[y]
        z += 1
        y += 1

array = [5, 3, 2, 7, 8, 4, 6, 1]

print("정렬되지 않은 리스트 : ", array)
mergesort(array)
print("정렬된 리스트 : ", array)
