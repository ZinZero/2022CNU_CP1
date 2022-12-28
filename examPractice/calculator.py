a = int(input("A 입력 : "))
b = int(input("B 입력 : "))


def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def mul(x, y):
    return x * y

def divide(x, y):
    return float(x / y)

def squre(x):
    return x * x

print("더하기 : ", add(a, b))
print("빼기 : ", minus(a, b))
print("곱하기 : ", mul(a, b))
print("나누기 : ", divide(a, b))
print("a 제곱 : ", squre(a))
print("b 제곱 : ", squre(b))
