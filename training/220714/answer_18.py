word = 'banana'

# 1. 풀이
result = {}
for char in word:
    # 딕셔너리에 키가 있으면?
    if not char in result:
        # 키랑 값이랑 1으로 초기화한다.
        result[char] = 1
    # 딕셔너리에 키가 없으면?
    else:
        result[char] = result[char] + 1
print(result)

# 2. 풀이

result = {}
for char in word:
    # result['a'] 없으면 KeyError
    # result.get('a') 기본값이 None
    # result.get('a', 0) 기본값이 0
    result[char] = result.get(char, 0) + 1
print(result)

# 출력부분
for key in result:
    print(key, result[key])
    