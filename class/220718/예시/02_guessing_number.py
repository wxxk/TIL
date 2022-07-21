# 숫자 입력을 받아서 출력
numbers = input('숫자를 입력해주세요: ')
print(numbers)

try: # 밑에를 시도해보고
    if int(numbers) == 5:
     print('오오~')
    else:
     print('오가 아닙니다.')

except: # 예외가 발생하면
    print('숫자를 입력하지 않았습니다.')