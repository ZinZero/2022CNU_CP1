data = input('입력해주세요: ')

datelist = data.split(',')

print('학번 : ', datelist[0])
print('이름 : ', datelist[1])
print('메일 : ', datelist[2])
print('정보의 개수: ', len(datelist))