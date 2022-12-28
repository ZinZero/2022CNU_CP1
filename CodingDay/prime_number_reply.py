import sys


number = int(sys.stdin.readline())
answer = 0
num_list = [i for i in range(number + 1)]

for i in range(2, number + 1):
    for j in range(2 * i, number + 1, i):
        if num_list[j] != 0:
            num_list[j] = 0


for i in num_list[2:]:
    if i != 0:
        answer += 1

print(answer)

# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 출력하시오.