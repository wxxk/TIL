import sys
sys.stdin = open('input.txt', 'r')

a, b = map(int, input().split())
print (a + b)
print (a - b)
print (a * b)
print (int(a / b))