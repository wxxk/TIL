import sys
sys.stdin = open('2058.txt', 'r')

n = int(input())
result = 0

while n:
    result += n%10
    n //=10

print(result)
