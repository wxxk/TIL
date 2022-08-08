A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    # 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
X = 0
Y = 0
for x in range(3):
    for y in range(3):
        # x, y => 0, 0 ~ 3, 3
        # x, y = 1, 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                X = nx
                Y = ny
                print(X, Y)
                print(A[X][Y])
        print()