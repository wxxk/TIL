# 1. num은 input으로 사용자에게 입력 받으세요.
num = int(input())
print(num, type(num))
# print(num) (중간 확인 절차)
# 2. 조건문을 통해서 홀수/짝수 여부를 출력하세요
# 숫자로서의 num!
if num % 2 == 1:
    print('홀수')
else:
    print('짝수')