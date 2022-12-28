ce = input("입력 : ")

argv = ce.replace("\"", "").split(" ")

dict = {}

dict[argv[1].replace("-", "").split("=")[0]] = argv[1].split("=")[1]
dict[argv[2].replace("-", "").split("=")[0]] = argv[2].split("=")[1]
dict[argv[3].replace("-", "").split("=")[0]] = argv[3].split("=")[1]

print("argc : ", len(argv))
for i in range(0, len(argv)):
    print("argc[", i, "] : ", argv[i])

print(dict.keys())
print(dict.values())
