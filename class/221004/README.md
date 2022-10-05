# Django CRUD
> Django : 파이썬기반 웹 프레임워크

## 1. 가상황경 및 Django 설치
> 가상환경 : 프로젝트 별 별도 패키지 관리


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
> Django : 주요 기능 단귀 App구조, App 별로 MTV를 구조를 가지는 모습 + `urls.py`

### 1. app 생성
```bash
$ python manage.py startapp app_name
```

### 2. app 등록
* `settings.py` 파일의 `INSTALLED_APPS`에 추가
```python
INSTALLED_APPS = [
  'articles',
  ...
]
```

### 3. urls.py 설정
```python
# 프로젝트/urls.py
```

```python
# articles/ulrs.py
```

## 3. Index
> url을 등록하고, view 함수 생성, template 만든다.

## 4. CRUD 

### 0. ModelForm 선언
> 선언된 모델에 따른 필드 구성 (1) form 생성 (2) 유효성 검사
```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

  class Meta:
    model = Article
    fields = ['title', 'content']
```

### 1. model 정의(DB 설계)

#### 1. 클래스 정의

#### 2. 마이그레이션 파일 생성

#### 3. DB반영(`migtate`)

### 1. CRUD 기능 구현

#### 1. Create (사용자가 게시글 생성)
> 사용자에게 HTML Form 제공해주고, 입력한 데이터를 처리
##### 1. HTML Form 제공
> http://127.0.0.1:8000/articles/new/

###### (1) urls.py

###### (2) views.py
```python
def create(request):
  article_form = ArticleForm()
  context = {
    'article_form' : article_form
  }
  return render(request, 'articles/create.html', context=context)
```

###### (3) articles/create.html
```django
{{ article_form.as_p }}
```


##### 2. 입력받은 데이터 처리
> http://127.0.0.1:8000/articles/create/
> 게시글 DB에 생성하고 index 페이지로 redirect

#### 2. 게시글 목록
> DB에서 게시글을 가져와서, template에 전달