a = 5 # int
b = '5' # str
print(a, type(a))
print(b, type(b))

#길이- len
fruit = 'abcde'
print(len(fruit)) # 5

# 접근
print(fruit[1]) # b
# 컴퓨터에서는 숫자를 0부터

# 인덱싱
print(fruit[1:3]) ## bc
# 인덱스 1이상, 3 미만
# a b c d e
# 0 1 2 3 4

# 마지막 값은???
# 파이썬은 음의 인덱스도 가지고 있다!
print(fruit[len(fruit)-1])
print(fruit[-1])