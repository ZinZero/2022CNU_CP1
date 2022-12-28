pay = int(input("물건 값 : "))

change = 1000 - pay
print("거스름돈 : ", change)

myCoin = [500, 100, 50, 10]

change_list = []

while change != 0:
    for i in myCoin:
        r = 0
        r += change // i
        change_list.append(r)
        change -= r * i

print("최소 동전 개수 : ", sum(change_list))
