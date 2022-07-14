word = input()

for i in word:
    i = ord(i) - 32
    i = chr(i)
    print(i, end="")