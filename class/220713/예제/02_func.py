def foo():
    # 하나의 값만 return하고 함수 실행이 종료
    return ''
    #도달할 수 없는 코드
    return ''



def minus_and_product(x, y):
    return x - y, x * y

result = minus_and_product(4, 5)
print(result, type(result))
# 두개의 값이 아니라 하나의 튜플만 반환됨



def no():
    a = 1

result = no()
print(result, type(result)) # None <class 'NoneType'>



# print 함수는
# 출력을 해주고, return 값은 없습니다. (None)
a = print('hi')
print(a, type(a)) # None <class 'NoneType'>