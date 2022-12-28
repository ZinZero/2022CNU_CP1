ce = input("입력 : ")

info = ce.replace("{", "").replace("\"", "").replace("}", "").split(",")

infoDict = {}

infoDict2 = {'university': info[0].split(":")[1], 'grade': info[1].split(":")[1], 'major': info[2].split(":")[1],
             'position': info[3].split(":")[1]}

infoDict[info[0].split(":")[0]] = info[0].split(":")[1]
infoDict[info[1].split(":")[0]] = info[1].split(":")[1]
infoDict[info[2].split(":")[0]] = info[2].split(":")[1]
infoDict[info[3].split(":")[0]] = info[3].split(":")[1]

print("학교 : ", infoDict['university'])
print("학년 : ", infoDict['grade'])
print("전공 : ", infoDict['major'])
print("구성원 : ", infoDict['position'])

print(infoDict.keys())
print(infoDict.values())
