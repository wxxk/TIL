import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    if a > b:
        print(f'#{i} >')
    elif a == b:
        print(f'#{i} =')
    else:
        print(f'#{i} <')