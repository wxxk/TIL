# 2222 / 02 / 28
import sys
sys.stdin = open('2056.txt', 'r')

T = int(input())

for i in range(1, T+1):
    n = list(map(int, input()))
    year = n[0:4]
    month = n[4:6]
    day = n[6:]
    print(year)
    # if (month in ['01', '03', '05', '07', '08', '10', '12']) and (int(day) <= 31):
    #     print('#{} {}/{}/{}'.format(i, year, month, day))
    # elif (month in ['04' '06' '09' '11']) and (int(day) <= 30):
    #     print('#{} {}/{}/{}'.format(i, year, month, day))
    # elif (month in ['02']) and (int(day)) <= 28:
    #     print('#{} {}/{}/{}'.format(i, year, month, day))
    # else:
    #     print('#{} -1'.format(i))