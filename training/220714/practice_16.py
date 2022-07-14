word = input()
cnt = 0

for i in word:
    if i in ['a', 'e', 'i', 'o', 'u']:
        cnt += 1
print(cnt)