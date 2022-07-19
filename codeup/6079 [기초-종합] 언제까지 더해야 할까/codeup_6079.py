n = int(input())
sum = 0
for i in range(0, n):
    if sum < n:
        sum += i
        if sum >= n:
            print(i)
            break