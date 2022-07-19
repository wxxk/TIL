a, b, c = map(int, input().split())
# 3 7 9
d = 1

while d%a!=0 or d%b!=0 or d%c!=0 :
    # False이 나오면 벗어남
    # 63%3=0 / 63%7=0 / 63%=0 -> 다 True 값(!= : True일 경우 False)
  d += 1
print(d)