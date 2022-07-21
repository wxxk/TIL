import sys
sys.stdin = open('1989.txt', 'r')

T = int(input())

for i in range(1, T+1):
    word = input()
    # print(word[::-1])
    if word == word[::-1]:
        print('#{} {}'.format(i, 1))
    else:
        print('#{} {}'.format(i, 0))