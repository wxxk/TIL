n = int(input())
result = 0

while n:
    result += n%10
    n = n//10
    if n != 0:
        result *= 10

print(result)