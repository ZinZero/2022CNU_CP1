import random
import math
import sys

print("입력해주세요 : ", end='')
x = int(sys.stdin.readline())

number = []

for i in range(x+1):
    ren = random.randrange(1, 11)
    while ren in number:
        ren = random.randrange(1, 11)
    number.append(ren)

    if len(number) == x:
        break

print("리스트1 : ", number)

print("최댓값 : ", max(number))
print("최솟값 : ", min(number))
print("제곱의 합 : ", math.pow(max(number), 2) + math.pow(min(number), 2))
