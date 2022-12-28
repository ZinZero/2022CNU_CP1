input_number = int(input())

number = input_number

list1 = [[0 for _ in range(number)] for _ in range(number)]

col = -1
row = 0
value = 1

direction = 1

while number > 0:
    for i in range(number):
        col += direction
        list1[row][col] = value
        value += 1
    number -= 1
    for j in range(number):
        row += direction
        list1[row][col] = value
        value += 1
    direction *= -1

for i in range(input_number):
    for j in range(input_number):
        print(list1[i][j], end=' ')
    print()

# 2차원 배열 (nXn)이 있을 때 n을 입력받아 달팽이 모양으로 커지는 배열을 만드시오.
# 조건1) 숫자는 시계방향으로 배열한다.
# 조건2) 배열할 숫자는 1부터 n까지이다.
# 조건3) 입력할 수 있는 숫자 n의 범위는 1부터 100까지이다.