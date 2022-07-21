import sys
sys.stdin = open('1288.txt', 'r')

T = int(input())

for i in range(1, T+1):
    number = int(input())
    list = [0]*10
    a = 0
    while (True):
        if 0 in list: # 리스트에 0이 있으면 number를 리스트
            a += 1
            num = str(number * a)
            for j in range(len(num)):
                list[int(num[j])] = 1
        else:
            break
    print('#{} {}'.format(i, num))