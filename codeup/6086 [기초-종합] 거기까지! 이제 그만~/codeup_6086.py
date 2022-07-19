n = int(input())
c = 0
s = 0

while True:
    s += c
    c += 1
    if s >= n:
        print(s)
        break