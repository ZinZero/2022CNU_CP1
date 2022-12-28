import time


def search(t_list, target):
    t_list_length = len(m_list)

    left = 0
    right = t_list_length - 1

    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if t_list[mid] == target:
            return mid

        elif t_list[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return answer

m_list = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 134, 200, 300, 400, 500, 600, 666]

start = time.time()
print('리스트에서 값 600의 위치 : ', search(m_list, 600))
print('소요시간 : ', time.time() - start)

print()

start = time.time()
print('리스트에서 값 -1의 위치 : ', search(m_list, -1))
print('소요시간 : ', time.time() - start)
