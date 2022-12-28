unsorted_list = [5, 3, 2, 7, 8, 4, 6, 1]

def conquer_list(left, right):
    new_list = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            new_list.append(left[left_index])
            left_index += 1
        else:
            new_list.append(right[right_index])
            right_index += 1

    if left_index == len(left):
        new_list += right[right_index:]
    else:
        new_list += left[left_index:]

    return new_list


def merge_sort(list1):
    if len(list1) <= 1:
        return list1


    mid = len(list1) // 2
    left = merge_sort(list1[:mid])
    right = merge_sort(list1[mid:])

    return conquer_list(left, right)

print("정렬되지 않은 리스트 : ", unsorted_list)
print("정렬된 리스트 : ", merge_sort(unsorted_list))
