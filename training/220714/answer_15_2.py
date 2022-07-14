# 1. 리스트에 담는다!
word = 'banana'
result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        # 리스트에 축다해줘
        result.append(idx)
print(result)

# 2. 그때 그때 출력
word = 'banana'
result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx, end=' ')