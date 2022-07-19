n = int(input())
result = ''

d = [[0 for j in range(20)] for i in range(20)]

for k in range(n):
    a, b = map(int, input().split())
    d[a-1][b-1] += 1
    for i in range(20):
        result = d[i]
        
        print(' '.join(map(str, result)))