# 모음의 갯수
# a, e, i, o, u
word = 'apple'

# 지금은 인덱스가 필요없어서 그냥 char로 받음
count = 0

for char in word:
    if char in 'aeiou':
        count += 1 
print(count)