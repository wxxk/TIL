import sys
sys.stdin = open('2063.txt', 'r')

n = int(input())

numbers = list(map(int, input().split()))
number = numbers.sort()

mid = int(n / 2)
print(numbers[mid])
