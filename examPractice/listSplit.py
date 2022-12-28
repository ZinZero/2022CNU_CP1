information = input("입력을해주세요: ")

new_list = information.split(",")

print("학번 : ", new_list[0])
print("이름 : ", new_list[1])
print("메일 : ", new_list[2])
print("정보의 개수 : ", len(new_list))
