with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    fruits = text.split('\n')
    name = ''
    list = []
    # print(fruits, type(fruits))

    for i in fruits:
        if i[-5::] == 'berry':
            list.append(i)
    list_set = (set(list))
    print(len(list_set))
    for j in list_set:
        print(j)
    
with open('./data/02.txt', 'w', encoding='utf-8') as f:
     f.write(f'{len(list_set)}\n')
     for j in list_set:
        f.write(f'{j}\n')
    
