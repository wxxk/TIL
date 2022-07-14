word = input()
dict = { }

for i in (word):
    if dict.get(i) == None:
        dict[i] = 1
    elif dict.get(i) != None:
        dict[i] += 1

for k, v in dict.items():
    print(k, v)