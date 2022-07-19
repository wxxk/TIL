c = ord(input())
t = ord('a')

while t <= c: # t가 c보다 작거나 같다 = True이면 while문 반복 / False 문 while문 종료
    print(chr(t), end=' ')
    t += 1