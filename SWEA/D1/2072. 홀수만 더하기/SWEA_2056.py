import sys
sys.stdin = open('2056.txt', 'r')

T = int(input())

for i in range(1, T+1):
    date = str(input())

    year = date[:4]
    month = date[4:6]
    day = date[6:]

    year_int = int(date[:4])
    month_int = int(date[4:6])
    day_int = int(date[6:])

    if month in ['01', '03', '05', '07', '08', '10', '12']:
        if day_int > 31:
            print('#{} {}'.format(i, -1))
        else:
            print('#{} {}/{}/{}'.format(i, year, month, day))

    elif month in ['04', '06', '09', '11']:
        if day_int > 11:
            print('#{} {}'.format(i, -1))
        else:
            print('#{} {}/{}/{}'.format(i, year, month, day))
    elif month == '02':
        if day_int > 28:
            print('#{} {}'.format(i, -1))
        else:
            print('#{} {}/{}/{}'.format(i, year, month, day))
    else:
        print('#{} {}'.format(i, -1))