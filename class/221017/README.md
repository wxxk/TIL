# 이미지 업로드

### [기본설정](#기본설정)

- 모델 설정 : `upload_to`
- URL 설정 : `MEDIA_ROOT, MEDIA_URL`



### 이미지 업로드(CREATE)

- [모델 설정](#모델 설정)
- [HTML 설정](#HTML 설정)
- [View 설정](#View 설정)



### 이미지 업로드(READ)

- img 태그활용



### 이미지 업로드(UPDATE)

- 이미지 수정하기



### 이미지 Resizing

- Django-imagekit

---

### 기본설정

- ImageField

  - 이미지 업로드에 사용하는 모델 필드

  - FileField를 상속받는 서브 클래스 / FileField의 모든 속성 및 메서드를 사용 가능

  - ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성

    max_length 인자를 사용하여 최대 길이를 변경

  `[주의] 사용하려면 반드시 Pillow라이브러리가 필요`



###### 모델 설정

```python
# models.py
image = models.ImageField(upload_to='images/', blank=True)
```

- 이미지 Resizing 까지 같이 해주기!!



###### URL 설정

- MEDIA_ROOT
  - 사용자가 업로드 한 파일들을 보관할 디렉토리의 절대경로
  - django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
- MEDIA_URL
  - MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
  - 업로드 된 파일의 주소를 만들어 주는 역할
  - 비어있지 않은 값으로 설정 한다면 반드시 `/`로 끝나야 함

```python
# settings.py
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'



# [프로젝트이름]/urls.py
'''
사용자가 업로드 한 파일이 우리 프로젝트에 업로드 되지만,
실제로 사용자에게 제공하기 위해서 업로드 된 파일의 URL이 필요함
'''
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settgins.MEDIA_ROOT)
```





---

### 이미지 업로드

###### 모델 설정

- ImageField
  - `upload_to='images/'` : 실제 이미지가 저장되는 경로를 지정
- blank=True
  - 이미지 필드에 빈 값이 허용되도록 설정(이미지를 선택적으로 업로드 가능)

```python
## articles/models.py

class Article(models.Model):
    ...
    image = models.ImageField(blank=True, upload_to='images/')
```

```bash
# 마이그레이션 실행
$ python manage.py makemigrations

$ pip instaill Pillow

$ python manage.py makemigrations
$ python manage.py migrate

$ pip freeze > requirements.txt
```

###### HTML 설정

- form 요소 - enctype(인코딩) 속성
  - multipart/form-data 
    - 파일/이미지 업로드 시에 반드시 사용해야 함 (전송되는 데이터의 형식을 지정) 
    - `<input type="file">`을 사용할 경우에 사용

```html
<!-- articles/create.html -->
<form action="" method='POST' enctype="multipart/form-data">
    {% csrf_token %}
    {% bootstrap_form form %}
    <input type="submit" class="btn btn-info text-white">
</form>
```

###### View 설정

- 업로드 한 파일은 reequest.FILES 객체로 전달

```python
# views.py
def create(request):
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("articles:index")
    else:
        form = ArticleForm()
    context = {
        "form": form,
    }
    return render(request, "articles/new.html", context)
```





---

### READ

###### img 태그 활용

- article.image.url == 업로드 파일의 경로
- article.imgae == 업로드 파일의 파일 이름

```html
{% if article.image %}
	<img src="{{ article.image.url }}" alt="{{ article.image }}">
{% endif %}
```





---

### UPDATE

###### 이미지 수정하기

```HTML
<!-- articles/update.html -->

<!-- enctype="multipart/form-data" -->
<form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {% bootstrap_form article_form %}
    <input type="submit" class="btn btn-info text-white">
</form>
```

```python
# view.py

# request.FILES
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:detail", article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        "article_form": article_form,
        "article": article,
    }
    return render(request, "articles/update.html", context)
```





---

### 이미지 Resizing

###### Django-imagekit

- 실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 작업

- `<img>` 태그에서 직접 사이즈를 조정할 수도 있지만, 

  업로드 될 때 이미지 자체를 resizing 하는 것을 사용해 볼 것

- django-imagekit 라이브러리 활용

```bash
# 1. django-imagekit 설치
$ pip install django-imagekit

$ pip freeze > requirements.txt
```

```python
# 2. INSTALLED_APPS에 추가
# settings.py

INSTALLED_APP = [
    ...
    'imagekit',
    ...
]



# 3. 이미지 크기 변경하기
# models.py

'''
ProcessedImageField()의 parameter로 작성된 값들은
변경이 되더라도 다시 makemigrations를 해줄 필요없이 즉시 반영 됨
'''

from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(400, 300)],
        format="JPEG",
        options={"quality": 80},
    )
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

