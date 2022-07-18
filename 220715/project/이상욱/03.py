with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = text.split('\n')
    result = {}

    for char in fruits:
        result[char] = result.get(char, 0) + 1

for i in result:
    print(i, result[i])

with open('./data/03.txt', 'w', encoding='utf-8') as f:
    for i in result:
        f.write(f'{i}, {result[i]}\n')