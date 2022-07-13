# numbers = [0, 20, 100]
# numbers = [0, 20, 100, 50, -60, 50, 100]
# numbers = [0, 1, 0]
numbers = [-10, -100, -30]
max_num = numbers[0]

for n in numbers:
    if max_num < n: 
        max_num = n
print(max_num)