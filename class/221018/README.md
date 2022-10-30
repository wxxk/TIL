# A one-to-many relationship

### [1. Foreign Key](#1. Foreign Key)



### [2. 모델 관계 설정](#2. 모델 관계 설정)



### [3.Comment](#3.Comment)

- ##### [모델 정의](#모델 정의)

- ##### [Migration](#Migration)



### [4. 관계 모델 참조](#4. 관계 모델 참조)

- ##### [역참조](#역참조)

- ##### [ForeignKey arguments – related_name](#ForeignKey arguments – related_name)

- ##### [admin site 등록](#admin site 등록)



### [5. Comment 구현](#5. Comment 구현)

- ##### [CREATE](#CREATE)

- ##### [READ](#READ)

- ##### [DELETE](#DELETE)



### 6. Comment 추가 사항

- ##### [댓글 개수 출력하기](#댓글 개수 출력하기)

- ##### [댓글이 없는 경우 대체 컨텐츠 출력](#댓글이 없는 경우 대체 컨텐츠 출력)

---

### 1. Foreign Key

##### 개념

- 외래 키
- 관계형 데이터베이스에서 다른 테이이블의 행을 식별할 수 있는 키
- 참조되는 테이블의 **기본 키**를 가르킴
- 참조하는 테이블의 행 1개의 값은, 참조되는 측 테이블 행 값에 대응됨
- 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음

##### 특징

- 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
  - 참조 무결성 : 데이터 베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
    - 외래 키가 선언된 테이블의 외래 키 속성의 값은 해당 테이블의 기본 키 값으로 존재
- 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함





---

### 2. 모델 관계 설정

- 게시판의 게시글과 1:N 관계를 나타낼 수 있는 댓글 구현
- 1:N 관계에서 댓글을 담당할 Article 모델은 1, Comment 모델은 N이 될것
  - 게시글은 댓글을 0개 이상 가진다
    - 게시글(1)은 여러 개의 댓글(N)을 가진다
    - 게시글(1)은 댓글을 가지지 않을 수도 있다.
  - 댓글은 반드시 하나의 게시글에 속한다.

##### Django Relationship fields 종류

- OneToOneField() : A one-to-one relationship
- ForeignKey() : A one-to-many relationship
  - Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당
  - 2개의 필수 위치 인자가 필요
    - 참고하는 `model class`
    - `on_delete`옵션
      - CASCADE : 부모 객체가 삭제 됐을 떄 이를 참조하는 객체도 삭제
      - PROECT, SET_NULL, SET_DEFAULT 등 여러 옵션 값들 존재
- ManyToManyField() : A many-to-many relationship





---

### 3.Comment

##### 모델정의

- 외래 키는 필드 ForeignKey 클래스를 작성하는 위치와 관계없이 **필드의 마지막**에 작성
- ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 **단수형**으로 작성 권장

```python
# articles/models.py

class Comment(models.Model):
	content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

##### Migration

```bash
# models.py에서 모델에 대한 수정사항이 발생했기 때문에 migrations 과정을 진행
$ python manage.py makemigrations
$ python manage.py migrate
```





---

### 4. 관계 모델 참조

##### 역참조

- 나를 참조하는 테이블을 참조하는 것
- 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
- 1:N 관계에서는 1이 N을 참조하는 상황
- `article.comment_set.method()`

##### ForeignKey arguments – related_name

- 역참조 시 사용하는 매니저 이름(`model_set manager`)을 변경할 수 있음
- 작성 후, migation 과정 필요
- 선택 옵션이지만 상황에 따라 반드시 작성

```python
# related_name 설정
class Comment(models.Model):
	...
    article models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment")
    
# 기본 article.comment_set은 더 이상 사용할 수 없고,
# article.comments로 대체됨
```

##### admin site 등록

```python
# articles/admin.py

from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
```





---

### 5. Comment 구현

##### CREATE

- 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 작성

```python
# articles/forms.py

from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        # 외래키 필드 출력에서 제외
        exclude =('article',)
        
```

- detail 페이지에서 CommentForm 출력 (view 함수)

```python
# articles/views.py

from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

- detail 페이지에서 CommentForm 출력(템플릿)

```html
<!-- articles/detail.html -->
...
{{ comment_form }}
...
```

- url을 통해 변수 넘기기

```python
# articles/urls.py

urlpatterns = [
	...,
	path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]



# articles/views.py

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # article 객체를 저장하지 못함
        # 데이터 베이스에 저장히기 전에 객체에 대한 추가적인 작업을 진행할 수 있도록
        # 인스턴스만은 반환해 주는 옵션 값을 제공
        comment = comment_form.save(commit=False)
        comment.article = article
        comment_form.save()
    return redirect('articles:detail', article.pk)
```



##### READ

- 작성한 댓글 목록 출력하기

```python
# articles/views.py

from .model import Article, Comment

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    
    #특정 article에 있는 모든 댓글을 가져온 후 
    comments = article.comment_set.all()
    
    context = {
        'article': article,
        'comment_form': comment_form,
        
        # context에 추가
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)
```

- detail 템플릿에서 댓글 목록 출력하기

```html
<!-- articles/deatil.html -->
...
{% for comment in comments %}
	{{ comment.content }}
{% endfor %}
...
```



##### DELETE

- 댓글 삭제 구현하기

```python
# articles/urls.py

urlpatterns = [
	...,
	path(
        '<int:article_pk>/comments/<int:comment_pk>/delete/', 							views.comments_delete,
        name='comments_delete'
    ),
]




# articles/views.py

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

- 댓글을 삭제할 수 있는 버튼을 각각의 댓글 옆에 출력

```html
<!-- articles/deatil.html -->
...

{% for comment in comments %}
	{{ comment.content }}
	<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
		{% csrf_token %}
		<input type="submit" value="DELETE">
	</form>
{% endfor %}

...
```





---

### 6. Comment 추가 사항

##### 댓글 개수 출력하기

- DTL filter - length 사용

```html
<!-- articles/detail.html -->
{% if comments %}
	<p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
{% endif %}

<!-- ------------------------------------------------------------ -->
{% if article.comment_set.all|length %}
	<p><b>{{ article.comment_set.all|length }}개의 댓글이 있습니다.</b></p>
{% endif %}
```

##### 댓글이 없는 경우 대체 컨텐츠 출력

- DTL for empty 활용하기

```html
<!-- articles/detail.html -->

{% for comment in comments %}
	{{ comment.content }}
	<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
		{% csrf_token %}
		<input type="submit" value="DELETE">
	</form>
{% empty %}
	<p>댓글이 없어요..</p>
{% endfor %}
```

