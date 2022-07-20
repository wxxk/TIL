import sys
sys.stdin = open('input.txt', 'r')

# A사 : W * P
# B사 : R이하 = Q
#       R초과 = Q + S*(W -R)

T = int(input())

for i in range(1, T+1):
    p, q, r, s, w = map(int, input().split())
    A = p * w
    B = q

    if w > r:
      B += s*(w-r)

    print(f'#{i} {min(A, B)}')
