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
            # num = 1295
            for j in range(len(num)): #num 숫자의 길이
                # range(len(num)) = range(0,4)
            
                list[int(num[j])] = 1
                # num[1] : 리스트 1번자리 = 1
                # num[2] : 리스트 2번자리 = 1
                # num[9] : 리스트 9번자리 = 1
                # num[5] : 리스트 5번자리 = 1
        else:
            break
    print('#{} {}'.format(i, num))