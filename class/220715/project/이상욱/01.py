with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = text.split('\n')
    print(len(fruits))