# numbers = [0, 20, 100] # 20
# numbers = [0, 20, 100, 50, -60, 50, 100] # 50
# numbers = [0, 1, 0] # 0
numbers = [200, 150, 130, 100, 50]
max_number = numbers[0]
second_number = numbers[0]

# 1. 전체  숫자를 반복
for n in numbers:
    # 만약에, n이 최대보다 크다면
    if max_number < n:
        #최대값이었던 것이 두번째 큰 수로
        second_number = max_number
        max_number = n
    elif second_number < n < max_number:
        second_number = n
print(second_number)
