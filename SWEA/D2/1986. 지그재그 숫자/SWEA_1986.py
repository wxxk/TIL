import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    n = int(input())
    result = 0
    for j in range(1, n+1):
        if j%2 == 0:
            result -= j
        elif j%2 !=0:
            result += j
    print(f'#{i} {result}')