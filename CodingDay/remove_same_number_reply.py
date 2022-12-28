a = input() # 1 1 2 4 7 4 3
num_list = list(map(int, a.split(" ")))
# num_list = a.split(' ')

#num_list = []
#for i in a.split(' '):
#    num_list.append(int(i))

new_list = []

for k in num_list:
    if k not in new_list:
        new_list.append(k)

print(new_list)

# 여러 숫자들이 주어질 때, 같은 숫자가 있다면 같은 숫자는 1개만 남기고 모두 제거하ㅑ고, 그 결과 값을 리스트의 형식으로 출력하시오.