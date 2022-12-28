number = int(input())

k = number
space = 0
for _ in range(number//2):
    print(' ' * space, end='')
    print('*' * k)
    k -= 2
    space += 1

print(' ' * space, end= '')
print('*')

for _ in range(number//2):
    k += 2
    space -= 1
    print(' ' * space, end='')
    print('*' * k)

# 숫자 n을 입력받아, 모래시계 형태로 * 출력하기
# 조건1) 모래시계의 세로 크기는 n이다.
# 조건2) 모래시계는 n부터 1까지 작아지고, 다시 n까지 커지는 형태로 출력된다.
# 조건3) 모래시계에 입력되는 n은 무조건 홀수이다.