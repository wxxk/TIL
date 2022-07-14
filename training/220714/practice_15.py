# 문자의 위치 구하기
word = input()
a = -1

for i in word:
    a += 1
    if i == 'a':
        print(a)
        break

if len(word)-1 == a:
    print(-1)