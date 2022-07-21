import sys
sys.stdin = open('2072.txt', 'r')

T = int(input())

for i in range(1, T+1):
    sum = 0
    numbers = list(map(int, input().split()))
    for j in numbers:
        if j%2 != 0:
            sum = sum + j
    print('#{} {}'.format(i, sum))