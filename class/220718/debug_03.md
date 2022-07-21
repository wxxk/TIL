### 예외

- 실행 도중 예상치 못한 상황을 맞이하면 프로그램 실행을 멈춤
  - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러

- 실행 중에 감지되는 에러들을 예외라고 부름

- 예외는 여러 타입으로 나타나고, 타입이 메시지의 일부로 출력됨
  - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
- 모든 내장 예외는 Exception Class를 상속 받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음



### 예외 처리

- try 문 / except 절을 이용하여 예외 처리를 할 수 있음

#### try문

- 오류가 발생할 가능성이 있는 코드를 실행
- 예외가 발생되지 않으면, except 없이 실행 종료

#### except 문

- 예외가 발생하면, except 절이 실행
- 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

#### 예시

```python
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
    
#------------------------------------------
# 100을 사용자가 입력한 숫자로 나눠서 결과를 출력

numbers = input()

try: # 각 에러들을 명시해 줄수 있다.
    print(100/int(numbers))
    
except exception: #exception은 오류의 가장 상위 개념
    print('오류') # 상위의 개념으로 묶어버리면 밑에 실행 불가 / 사용할꺼면 맨 아래에 사용해야함
    
except ZeroDivisionError:
    print('0으로 나눌 수는 없습니다.')
    
except ValueError:
    print('숫자 형식을 입력해주세요.')
```



### 정리

- try : 코드를 실행함

- except : try 문에서 예외가 발생 시 실행함

- else : try 문에서 예외가 발생하지 않으면 실행함

- finally : 예외 발생 여부와 관계없이 항상 실행함

  ```python
  try:
      f = opne('file.txt')
  except FileNotFoundError:
      print('해당 파일이 없습니다.')
  else:
      print('파일을 읽기 시작합니다.')
      print(f.read())
      print('파일을 모두 읽었습니다.')
      f.close()
  finally:
      print('파일 읽기를 종료합니다.')
  ```

