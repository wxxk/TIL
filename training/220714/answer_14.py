# 문자의 갯수 구하기
# a 카운트

word = input()
count = 0

# i는 이름 붙이기
# 
for i in word:
    if i == 'a':
        count += 1

print(count)