import sys
import math
import random
print("입력해주세요 : ", end='')
x = int(sys.stdin.readline())

Number = []

for i in range(x+1):
    ren = random.randrange(1, 11)
    while ren in Number:
        ren = random.randrange(1, 11)
    Number.append(ren)

    if int(len(Number)) == x:
        break

print("리스트 1:", Number)

print("최댓값 : ", max(Number))
print("최솟값 : ", min(Number))
print("제곱의 합 : ", math.pow(max(Number), 2)+ math.pow(min(Number), 2))