import sys
sys.stdin = open('2025.txt', 'r')

n = int(input())
result = 0

for i in range(n+1):
    result += i
    
print(result)

