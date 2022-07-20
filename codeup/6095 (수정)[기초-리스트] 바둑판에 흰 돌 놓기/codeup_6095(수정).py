d=[]
for i in range(20) :
    d.append([])
    for j in range(20) : 
        d[i].append(0)

n = int(input())
for k in range(n):
    x, y = map(int, input().split())
    d[x][y] = 1

for i in range(1, 20) :
    for j in range(1, 20) : 
        print(d[i][j], end=' ')
    # 한 가로줄의 상황이 모두 출력되면
    # 다음 가로줄의 상황을 출력하기 위해 
    # 다음줄로 넘어간다
    print()
