import sys
sys.stdin = open('1976.txt', 'r')

T = int(input())

for i in range(1, T+1):
    time = list(map(int, input().split()))
    hour = time[0] + time[2]
    min = time[1] + time[3]

    if min > 60:
        hour += 1
        min -= 60
    if hour > 12:
        hour -= 12

    print('#{} {} {}'.format(i, hour, min))