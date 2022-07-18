word = "HappyHacking"

count = 0

for char in word:
    if char in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print(count)