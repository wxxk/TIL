n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d=[]
for i in range(23):
    d.append(0)

for i in range(n-1, -1, -1):
    print(a[i], end=' ')
    # list
    #  0 1 2 3 4 5 6 7 8 9  <- n-1은 9 : 여기부터 출력 
    # 10 4 2 3 6 6 7 9 8 5