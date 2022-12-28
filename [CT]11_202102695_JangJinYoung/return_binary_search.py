def binarySearch(array, target, left, right):
    if target not in array:
        print("리스트에 존재하지 않는 값 : ", target)
        return

    index = (left + right) // 2
    middle = array[index]

    if middle == target:
        print('리스트에서', target, '의 위치 : {}'.format(index))
        return
    elif middle > target:
        return binarySearch(array, target, left, right - 1)
    else:
        return binarySearch(array, target, left + 1, right)


m_list = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 134, 200, 300, 400, 500, 600, 666]

binarySearch(m_list, 600, 0, len(m_list))
binarySearch(m_list, -1, 0, len(m_list))
