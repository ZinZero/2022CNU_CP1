ce = input("입력 : ")

info = ce.replace('\"', '').replace('{', '').replace('}', '').split(',')

info_dict = {}

info_dict['university'] = info[0].split(':')[1]
info_dict['grade'] = info[1].split(':')[1]
info_dict['major'] = info[2].split(':')[1]
info_dict['position'] = info[3].split(':')[1]

print('학교 : ', info_dict['university'])
print('학년 : ', info_dict['grade'])
print('전공 : ', info_dict['major'])
print('구성원 : ', info_dict['position'])

print(info_dict.keys())
print(info_dict.values())