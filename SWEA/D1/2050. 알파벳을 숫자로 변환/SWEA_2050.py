# 알파벳을 숫자로 전환
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1 2 3 4 5 6 7 8 9 10 ... 26
import sys
sys.stdin = open("input.txt", "r")

n = input()
result = 0

for i in n:
    result = ord(i)-64
    print(result, end=' ')