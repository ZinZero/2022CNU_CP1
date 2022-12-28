a = int(input("입력 : "))

for i in range(a):
    for j in range(a - i):
        print(" ", end="")
    for j in range(0, 2 * i + 1):
        print("*", end="")
    print("")

for j in range(a//2):
    for i in range(a):
        print(" ", end="")
    print("*" * (a//10 + 1))

for i in range((a//10) + 1):
    print("*" * (2 * a + 1))
