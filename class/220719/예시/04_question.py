# 얕은 복사
a = [1, 2, 3]
b = a
b[0] = 'hi'

# a를 출력
print(a)
# b를 출력
print(b)

# list 형변환 결과 : 사실은 list고 값도 같지만 다른 메모리 주소 결과 받아냄
c = [3, 4, 5]
d = list(c)
d[0] = 'hi'

# 슬라이싱
e = [4, 5, 6]
f = e[::]
f[0] = 'hi'

# 깊은 복사
a = [[1, 2], 2, 3]
b = list(a)
b[0][0] = 'hi'

print(a)
print(b)

import copy
a = [[1, 2,], 2, 3]
b = copy.deepcopy(a)
b[0][0] = 'hi'
print(a)
print(b)


# 얕은 복사
# 리스트 주소가 123
