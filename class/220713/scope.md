### 범위



#### 함수의 scope

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- scope(범위)
  - global scope : **코드 어디에서든 참조**할 수 있는 공간
  - local scope : 함수가 만든 scope, **함수 내부에서만 참조 가능**
- variable(변수)
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수



#### 객체 수명 주기

- built-in scope (print, sum, len)
  - 파이썬이 실행된 이후부터 **영원히 유지**
- global scope (직접 정의한 것)
  - **모듈이 호출된 시점** 이후 혹은 **인터프리터가 끝날 때**까지 유지
- local scope
  - **함수가 호출될 때 생성**되고, **함수가 종료될 때**까지 유지

- 예시

```python
def func():
	a = 20
	print('local', a)
    
func()
print('global', a)

# 결과
# local 20 

#---------------------------------------------------------------------------
# func() ----> print('global', a) 
# NameError: name 'a' is not defined
# a는 Local scope에서만 존재
```





#### 이름 검색 규칙

- 파이썬에서 사용되는 이름들은 이름공간에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
  - Local scope : 함수
  - Enclosed scope : 특정 함수의 상위 함수
  - Global scope : 함수 밖의 변수, Import 모듈
  - Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성
- 즉, 함수 내에서는 바깥 Scope의 변수에는 접근 가능하나 수정은 할 수 없음
- 예시

```python
a = 10

def test():
    a = 20
    print(a)

test()
print(a)

# 1. test 함수 안에가 Local영역 : a 값 20 출력
	# 함수 호출이 끝날 때 소멸(Global영역에 a와 다른 변수)
# 2. Enclosed 영역은 존재하지 않음
# 3. Global 영역에 a 존재 : a 값 10 출력

# 결과
20
10
```





