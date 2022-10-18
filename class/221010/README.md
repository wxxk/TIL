# Django

### [0. 용어정리](# 0. 용어정리)

### [1. 사전 설정](#1. 사전설정)

- [가상활경 설정 및 활성화](#가상환경 설정 및 활성화)

- [Django 설치(3.2.13 버전)](# [Django 설치)

- [프로젝트 생성](# 프로젝트 생성)
- [서버 실행](# 서버 실행)

- 메인페이지 확인 (localhost:8000)

- [앱 생성 및 앱 등록](# 앱 생성 및 앱 등록)

### [2. Template ingeritance](# 2. Template ingeritance)

- [템플릿 상속](# 템플릿 상속)

  - `{% exteds '' %}` (base.html)

  - `{% block content %}{% endblock content%}`

- [App URL mapping](# App URL mapping)
  - 앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법
- [템플릿 경로 변경](# 템플릿 경로 변경)
  - 폴더 구조를 `app_name/templates/app_name/`형태로 변경
  - URL tag -> {% url 'articles:index' %}



### [3. Variable routing 작성](# 3. Variable routing 작성)

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



### [4. model](# 4. model)

- [model 정의](# model 정의)

  > [Model Field](https://velog.io/@bungouk6829/Django-%EB%AA%A8%EB%8D%B8%EC%9D%98-%ED%95%84%EB%93%9C-%EA%B4%80%EA%B3%84%ED%98%95-%ED%95%84%EB%93%9C)

- [Migrations](# Migrations)

- [ModelForm](#ModelForm)



### [5. CRUD](# 5. CRUD)

> Create / Read / Update / Delete

- [CREATE](# CREATE)

  - [Create 구현](# Create 구현)

    > 사용자의 입력을 받을 페이지를 렌더링하는 함수 / 입력한 데이터를 DB에 저장하는 함수

    1. url 정의
    2. 함수 정의
    3. html 만들기(method 정의)
       1. index.html에 new페이지로 가는 하이퍼 링크 작성
       2. 게시글 작성 후 확인
       3. new.html에 form 정의

- [READ](# READ)

  - [index](# index)

  - [상세페이지](# 상세페이지)

    - 글의 번호(PK)를 활용해서 하나의 뷰 함수와 템플릿 파일로 대응

    - URL로 특정 게시글 조회할 수 있는 번호 받기

    - views에서 get을 통해 일치하는 값 받기

      > 오른쪽 pk는 variable routing을 통해 받은 pk,
      >
      > 왼쪽 pk는 DB에 저장된 레코드의 id 칼럼

    - detail.html 정의
    - index.html에 detail로 가는 하이퍼 링크 작성(pk값도 보내주기)
    - 글을 쓰고 나면 detail페이지가 보여지도록 create에 redirect 인자 변경

- [UPDATE](# UPDATE)

  - [Update 구현](# Update 구현)

    > 사용자의 입력을 받을 페이지를 렌더링 하는 함수 / 입력한 데이터를 DB에 저장하는 함수

  - Edit

    - url - edit정의 (pk)
    - views - 함수 정의
    - Edit.html - value값 사용 (수정할 값 form)
    - detail.html - Edit페이지 하이퍼링크

  - Update

    - url - Update정의 (pk)
    - views - 함수 정의()

- [DELETE](# DELETE)

  - [Delete 구현](# Delete 구현)
    - 삭제하고자 하는 특정 글을 조회 후 삭제
    - url 정의 (pk값으로 조회)
    - views정의 (pk값으로 get / delete / redirect)
    - templates에서 삭제버튼 정의(method='POST')



---

### 0. 용어정리

##### HTML form’s attributes

- action 
  - 입력 데이터가 전송될 URL을 지정
  - 데이터를 어디로 보낼 것인지 정하는 것이며 이 값은 반드시 유효한 URL이어야 함
  - 만약 이 속성을 지정하지 않으면 데이터는 현재 `form`이 있는 페이지의 URL로 보내짐
- method
  - 데이터를 어떻게 보낼 것인지 정의
  - 입력 데이터의 HTTP request methods를 지정
  - HTML form 데이터는 오직 GET방식과 POST방식으로만 전송
- name
  - form을 통해 submit했을 때 name속성에 설정된 값을 서버로 전송
  - 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근

- GET
  - 서버로부터 정보를 조회하는 데 사용
  - 데이터를 가져올 때만 사용해야 함
  - 데이터를 서버로 전송할 때 Query string Parameters를 통해 전송
    - 데이터는 URL에 포함되어 서버로 보내짐
  - 이러한 문자열은 `&`로 연결된 key=value 쌍으로 구성
    - ex) http://host:port/path?key=value&key=value



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



###### 앱 생성 및 앱 등록

```bash
# 앱 생성
$ python manage.py startapp articles

# 앱 등록
# settings.py
INSTALLED_APPS = [
    'articles',
]
```



---

### 2. Template ingeritance

###### 템플릿 상속

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- bootstrap CDN 작성 -->
<title>Document</title>
</head>
<body>
{% block content %}
{% endblock content %}
<!-- bootstrap CDN 작성 -->
</body>
</html
```

```html
<!-- index.html -->
{% extends 'base.html' %}		# 하위 템플릿이 부모 템플릿을 확장한다는 것을 알림	

{% block content %}				# 하위 템플릿에서 재지정할 수 있는 블록을 정의
<h1>만나서 반가워요!</h1>			# 하위 템플릿이 채울 수 있는 공간
{% endblock content %}
```



###### App URL mapping

```python
# firstpjt/urls.py
from django.contrib import admin
from django.urls import path, include		# include 함수사용

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
    # include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고,
    # 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달
]


# articles/urls.py
from django.urls import path	# django.urls의 path를 사용
from . import views				# 현재 app폴더 안에 views 사용

urlpatterns = [
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.hello),
]
```



###### 템플릿 경로 변경

```python
# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],		# 추가
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



---

### 3. Variable routing 작성

```python
# urls.py

urlpatthers = [
    ...,
    # path('hello/<str:name>/', views.hello)
    path('hello/<name>/', views.hello)
]
```





---

### 4. model

###### model 정의

```python
# articles/modes.py

class Article(models.Model):
    title = models.CharFiedl(max_length=10)
    content = models.TextField()
# 모델 클래스 == 테이블 스키마
# 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨
```



###### Migrations

```bash
$ python manage.py makemigrations

$ python manage.py migrate
```



###### ModelForm

- ModelForm 선언

  - forms 라이브러리의 ModelForm 클래스를 상속받음

  - 정의한 ModelForm 클래스 안에 Meta 클래스 선언

  - 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

- Meta Class

  - ModelForm의 정보를 작성하는 곳

  - ModelForm을 사용할 경우 참조 할 모델이 있어야하는데,

    Meta class의 model 속성이 이를 구성함

  - fields 속성에 `'__all__'`를 사용하여 모델의 모든 필드를 포함

  - exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정

```python
# articles/forms.py
from django improt forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
```





---

### 5. CRUD

##### Create

```python
## 첫번째 방법
# 클래스를 통한 인스턴스 생성
article = Article()

# 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
article.title = '제목'
article.content = '내용'

# 인스턴스 save 메서드 호출
article.save()


## 두번째 방법
# 인스턴스 생성시 초기 값을 함께 작성하여 생성
article = Article(title='제목', content='내용')
article.save()


## 세번째 방법
# 생성된 데이터가 바로 반환
Article.objects.create(title='제목', content='내용')
```

###### Create 구현

```python
# 1. url 정의
# articles/urls.py

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]

# 2. 함수 정의
# articles/views.py

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    article = Article(title=title, content=content)
    article.save()
    
    return redirect('articles:detail', article.pk)



# 3. Handling HTTp requests

# new와 create view 함수를 함침
# 각각의 역할은 request.method 값을 기준으로 나뉨
# articles/views.py

def create(request):
    if reqeust.mehthod == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, "articles/new.html", context)
# 불필요해진 new의 view 함수와 url path를 삭제
```

```html
<!-- templates/articles/index.html -->
<!-- new 페이지로 이동할 수 있는 하이퍼 링크 작성 -->
{% extends 'base.html' %}
{% block content %}
    <h1>Articles</h1>
    <a href="{% url 'articles:new' %}">NEW</a>
    <hr>
{% endblock content %}


<!-- templates/aricels/new.html -->
{% extends 'base.html' %}
{% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        <label for="title">Title: </label>
        <input type="text" name="title"><br>
        <label for="content">Content: </label>
        <textarea name="content"></textarea><br>
        <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```



##### READ

```python
# 전체 데이터 조회
Article.objects.all()

# 단일 데이터 조회
Article.objects.get(content='내용')

# 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
Article.objects.filter(content='내용')
```

###### index

```python
# articles/views.py
from .models import Article
def index(request):
    articles = Article.objects.all()	# article 전체 데이터를 조회
    context = {
    'articles': articles,				# context로 넘겨줌
    }
    return render(request, 'articles/index.html', context)
```

```html
<!--templates/articles/index.html-->
{% extends 'base.html' %}
{% block content %}
    <h1>Articles</h1>
    <hr>
    {% for article in articles %}
        <p>글 번호: {{ article.pk }}</p>
        <p>글 제목: {{ article.title }}</p>
        <p>글 내용: {{ article.content }}</p>
    <hr>
    {% endfor %}
{% endblock content %
```

###### 상세페이지

```python
# articles/urls.py

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
]


# articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)
```

```html
<!--templates templates/articles/detail.html -->
{% extends 'base.html' %}
{% block content %}
    <h2>DETAIL</h2>
    <h3>{{ article.pk }} 번째 글</h3>
    <hr>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <p>작성 시각: {{ article.created_at }}</p>
    <p>수정 시각: {{ article.updated_at }}</p>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}


<!-- templates/articles/index.html -->
{% extends 'base.html' %}
{% block content %}
<!-- detail로 가는 버튼 정의 -->
{% for article in articles %}
<a href="{% url 'articles:detail' article.pk %}">[detail]</a>
<hr>
{% endfor %}

{% endblock content %}
```





##### UPDATE

```python
# 수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
article = Article.objects.get(pk=1)

# article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
article = title = 'byebye'

# save() 인스턴스 메서드 호출
article.save()
```

###### Update 구현

- edit

```python
# articles/urls.py


urlpatterns = [
	path('<int:pk>/edit/', views.edit, name='edit'),
]


# articles/views.py
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/deit.html', context)
```

```html
<!-- articles/edit.html -->
<!-- html 태그의 value 속성을 사용해 기존에 입력 되어 있던 데이터를 출력 -->
<!-- textarea 태그는 value 속성이 없으므로 태그 내부 값으로 작성 -->
{% extends 'base.html' %}
{% block content %}
    <h1>EDIT</h1>
    <form action="#" method="POST">
        {% csrf_token %}
        <label for="title">Title: </label>
        <input type="text" name="title" value="{{ article.title }}"><br>
        <label for="content">Content: </label>
        <textarea name="content" cols="30" rows="5">{{ article.content }}</textarea>
        <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

<!-- articles/detail.html -->
<!-- detail.html에서 edit 페이지로 이동하기 위한 하이퍼 링크 작성 -->
{% extends 'base.html' %}
{% block content %}
    <form action="{% url 'articles:edit' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="text" value="{{ articles.title }}" name="title">
  		<input type="text" value="{{ articles.content }}" name="content">
        <input type="submit" value="UPDATE">
    </form>
{% endblock %}
```

- update

```python
# articles/urls.py • Update 로직 작성
urlpatterns = [
    ...
    path('<int:pk>/update/', views.update, name='update'),
]
# articles/views.py
def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
```

```html
<!-- articles/edit.html -->
{% extends 'base.html' %}
{% block content %}
<h1>EDIT</h1>
<form action="{% url 'articles:update' article.pk %}" method="POST">
{% csrf_token %}
...
<a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```

- ModelForm

```python
# edit과 update view 함수를 합침
# edit의 view 함수와 url pathfmf 삭제

# articles/views.py    
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
	    form = ArticleForm(request.POST, instance=article)
    	if form.is_valid():
        	form.save()
	        return redirect('articles:detail', article.pk)
	else:
        form = ArticleForm(instance=article)
    context = {
	    'form': form,
    	'article': article,
    }
    return render(request, 'articles/update.html', context)
```





##### DELETE

```python
# 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
article = Article.objects.get(pk=1)

# delete() 인스턴스 메서드 호출
article.delete()
```

###### Delete 구현

```python
# articles/urls.py

urlpatterns = [
    path('<int:pk>/delete/', views.delete, name='delete')
]


# articles/views.py

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

```html
<!-- articles/detail.html -->
<!-- delelte버튼 생성-->

{% extends 'base.html' %}
{% block content %}
<form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
</form>
{% endblock content %}
```



