a, b = map(int, input().split())
a = bool(a)
b = bool(b)

print(((not a) and (not b)) or (a and b))