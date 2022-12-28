a = int(input("A 입력 : "))
b = int(input("B 입력 : "))

def add(a, b):
    result1 = a + b
    return result1
print("더하기 : ", add(a, b))

def sub(a, b):
    result2 = a - b
    return result2
print("빼기 : ", sub(a, b))

def mul(a, b):
    result3 = a * b
    return result3
print("곱하기 : ", mul(a, b))

def division(a, b):
    result4 = a / b
    return result4
print("나누기 : ", division(a, b))

def square(a):
    result5 = a**2
    return result5
print("a의 제곱 : ", square(a))
print("b의 제곱 : ", square(b))