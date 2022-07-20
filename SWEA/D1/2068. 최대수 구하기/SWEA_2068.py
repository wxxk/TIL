import sys
sys.stdin = open('2068.txt', 'r')

n = int(input())

for i in range(1, n+1):
    numbers = map(int, input().split())
    numbers = max(numbers)
    print(f'#{i} {numbers}')