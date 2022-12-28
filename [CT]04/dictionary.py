ce = input("입력 : ")

arg = ce.replace("\"", "").split(' ')

arg_dict = {}

arg_dict[0] = arg[0].split(' ')[0]
arg_dict[1] = arg[1].split(' ')[0]
arg_dict[2] = arg[2].split(' ')[0]
arg_dict[3] = arg[3].split(' ')[0]

arg_dict2 = {}

arg_dict2['name'] = arg_dict[1].split('=')[1]
arg_dict2['ip'] = arg_dict[2].split('=')[1]
arg_dict2['port'] = arg_dict[3].split('=')[1]

print("argc : ", len(arg_dict))

print("argv[0] : ", arg_dict[0])
print("argv[1] : ", arg_dict[1])
print("argv[2] : ", arg_dict[2])
print("argv[3] : ", arg_dict[3])

print(arg_dict2.keys())
print(arg_dict2.values())