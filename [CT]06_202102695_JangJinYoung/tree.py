a = int(input())

for i in range(a):
    for j in range(a - i):
        print(' ', end='')
    for j in range(0, i*2 +1):
        print('*',end='')
    print('')

for j in range(1,6):
    for i in range(a):
        print(' ',end='')
    print('*' * (a //10 +1))

for i in range( (a // 10) + 1):
    print('*' * (2 * a + 1))