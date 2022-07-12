numbers = [0, 20, 100]
# numbers = [0, 20, 100, 50, -60, 50, 100]
# numbers = [0, 1, 0]
# numbers = [-10, -100, -30]
a = numbers[0]

for i in numbers:
    if i < a:
        a = i
print(a)

