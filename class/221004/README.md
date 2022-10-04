# Django CRUD

## 1. 가상황경 및 Django 설치

### 1. 가상환경 생성 및 실행

* 가상환경 폴더를 `.gitignore`로 설정을 해둔다.
```bash
$ python -m venv venv
$ source venv/Scripts/activate
```

### 2. Django 설치 및 기록

```
$ pip install django==3.2.13
$ pip freeze > requirements.txt
```

### 3. Django 프로젝트 생성
```bash
$ django-admin startproject pjt .
```


## 2. articles app 생성

### 1. app 생성

### 2. app 등록

### 3. urls.py 설정


## 3. Index
> url을 등록하고, view 함수 생성, template 만든다.

## 4. CRUD 

### 1. model 정의(DB 설계)

#### 1. 클래스 정의

#### 2. 마이그레이션 파일 생성

#### 3. DB반영(`migtate`)

### 1. CRUD 기능 구현

#### 1. Create (사용자가 게시글 생성)
> 사용자에게 HTML Form 제공해주고, 입력한 데이터를 처리
##### 1. HTML Form 제공
> http://127.0.0.1:8000/articles/new/

##### 2. 입력받은 데이터 처리
> http://127.0.0.1:8000/articles/create/
> 게시글 DB에 생성하고 index 페이지로 redirect

#### 2. 게시글 목록
> DB에서 게시글을 가져와서, template에 전달