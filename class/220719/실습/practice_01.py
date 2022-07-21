number = int(input())
result = 0

# number 가 0이 아니면 True
# number 가 0이되면 False
while number :
    result += number%10
    number //= 10

print(result)

#-----------------------------------
# 2.
# divmod(x, y)는 x를 y로 나누고,
# 결과를 tuple로 반환
# (몫, 나머지)

# number, remainder = divmod(number, 10)
# result += remainder
# print(result)