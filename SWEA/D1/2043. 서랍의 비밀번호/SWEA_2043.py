import sys
sys.stdin = open('2043.txt', 'r')

p, k = map(int, input().split())

cnt = 1
while p != k:
    k += 1
    cnt += 1

print(cnt)
