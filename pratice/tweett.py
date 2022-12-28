n1 = int(input())   #문제에서 주어진대로 입력받고~
n2 = int(input())
m = int(input())

count = 0   #그냥 선언해주고~

for i in range(n1, n2 + 1):     #여기서 출력! 입력받은 수부터 수까지니까 마지막에 +1
    print(i, end=" ")           #end사용해서 한 칸 띠우고 연속으로 쓰게 하고
    count += 1                  #반복문 한 번 돌 때 마다 1씩 증가~

    if count == m:              #증가하다가 입력받은 m이랑 같으면!!
        print("")               #줄바꿈~
        count = 0               #그리고 다시 0부터 시작
