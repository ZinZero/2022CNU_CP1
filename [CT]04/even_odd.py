number = input("숫자를 입력하세요 : ")

even = ( int(number) % 2 )

if int(even) == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")