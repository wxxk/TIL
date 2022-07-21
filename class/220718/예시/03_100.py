# 100을 사용자가 입력한 숫자로 나눠서 결과를 출력
from logging import exception

numbers = input()
try: # 각 에러들을 명시해 줄수 있다.
    print(100/int(numbers))
except exception: # 상위의 개념으로 묶어버리면 밑에 실행 불가
    print('오류')
except ZeroDivisionError:
    print('0으로 나눌 수는 없습니다.')
except ValueError:
    print('숫자 형식을 입력해주세요.')
