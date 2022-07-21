import sys
sys.stdin = open('1926.txt', 'r')

n = int(input())

for i in range(1, n+1):
    number = str(i) # 3, 6, 9의 갯수를 세기 위해 문자열로 바꿔줌
    cnt = 0
    
    cnt = number.count('3') + number.count('6') + number.count('9')

    if cnt == 0:
        print(i, end=' ')
    else:
        print('-'*cnt, end=' ') # '-'를 count의 갯수만큼 곱해줌