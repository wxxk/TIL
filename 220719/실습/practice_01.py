number = int(input())
result = 0

# number 가 0이 아니면 True
# number 가 0이되면 False
while number :
    result += number%10
    number //= 10

print(result)