# 여러 숫자들이 주얼질 떄, 같은 숫자가 있다면 같은 숫자는 1개만 남기고 모두 제거하고, 그 결과값을 리스트 형식으로 출력하시오.
# 조건1) 각각의 숫자들은 공백으로 구분되어 있다.
# 조건2) 출력되는 리스트는 숫자형으로 이루어진 리스트이다.


enter = input()

sp = enter.split(" ")

number = []
result = []

for i in range(0, len(sp)):
    number.append(int(sp[i]))


for j in number:
    if j not in result:
        result.append(j)

print(result)

