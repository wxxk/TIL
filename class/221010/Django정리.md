# Django

### [1. 사전 설정](#1. 사전설정)

- [가상활경 설정 및 활성화](#가상환경 설정 및 활성화)

- [Django 설치(3.2.13 버전)](# [Django 설치)

- [프로젝트 생성](# 프로젝트 생성)
- [서버 실행](# 서버 실행)

- 메인페이지 확인 (localhost:8000)



### [2. Variable routing 작성](# 2. Variable routing 작성)

> urls.py

- 변수는 `<>`에 정의하며 view 함수의 인자로 할당됨
- 기본 타입은 string이며 5가지 타입으로 명시할 수 있음
  1. str 
     - `/`를 지외하고 비어 있지 않은 몯느 문자열
     - 작성하지 않을 경우 기본 값
  2. int
     - 0 또는 양의 정수와 매치
  3. slug
  4. uuid
  5. path



3. Viwe 함수 작성









---

### 1. 사전설정

###### 가상환경 설정 및 활성화

```bash
$ python -m venv venv		# python -m venv [폴더명]

$ source venv/Script/activate		# 가상환경 활성화
```



###### Django 설치(3.2.13 버전)

````bash
$ pip install django==3.2.13

$ pip freeze > requirements.txt		# 패키지 목록 생성
````



###### 프로젝트 생성

```bash
$ djagno-admin startproject pjt .	# djagno-admin startproject [프로젝트이름] .
# .을 붙이지 않을 경우 현재 디렉토리에 프로젝트 디렉토리를 새로 생성(경로를 이동해서 실행)
# Project이름에는 python이나 django에서 사용중인 키워드 및 '-' 사용 불가
```



###### 서버 실행

```bash
$ python manage.py runserver
```



---

### 2. Variable routing 작성

```python
# urls.py

urlpatthers = [
    ...,
    # path('hello/<str:name>/', views.hello)
    path('hello/<name>/', views.hello)
]
```





---

### 3. Viwe 함수 작성