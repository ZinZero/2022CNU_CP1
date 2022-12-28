number = int(input("숫자를 입력하세요 : "))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n - 2)

print(fibonacci(number))
