# 값 초기화
n = 0
# 0부터 더하기 위해서
result = 0
# user_input 값
user_input = int(input())

# 1.
while n < user_input:
    print(f'n: {n}, result: {result}')
    n += 1
    result += n
print(result)

# 2.
n = 0
result = 0
user_input = int(input())
while n <= user_input:
    print(f'n: {n}, result: {result}')
    result += n
    n += 1
print(result)