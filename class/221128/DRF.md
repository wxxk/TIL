### Django Intro & Installation

```bash
$ pip install Django

$ pip install djangorestframework

$ django-admin startproject pjt

$ cd pjt

$ python manage.py runserver

$ python manage.py migrate

$ python manage.py startapp api

$ python manage.py createsuperuser
```





### View functions & URLS

```python
# api/views.py

from django.shortcuts import render, HttpResponse


def Index(request):
    return HttpResponse("It is working")


# pjt/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('api.urls')),
]
```

```python
# api앱에 urls.py 추가
# api/urls.py

from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index),
]

```





### Django Models

```python
# pjt/settings.py
INSTALLED_APPS = [
    ...
	'api',
]



# api/models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
```

```bash
$ python manage.py makemigrations

$ python manage.py migrate
```

```python
# api/admin.py
from django.contrib import admin
from .models import Article

admin.site.register(Article)	# admin 페이지에서 글 작성 가능



# api/models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
```

| ![화면 캡처 2022-11-28 161130](DRF.assets/화면 캡처 2022-11-28 161130.png) | ![화면 캡처 2022-11-28 161144](DRF.assets/화면 캡처 2022-11-28 161144.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |



```python
# api/admin.py

...


@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description')
```

| ![1](DRF.assets/1.png)                                       |
| ------------------------------------------------------------ |
|                                                              |
| ![화면 캡처 2022-11-28 161751](DRF.assets/화면 캡처 2022-11-28 161751.png) |



###  Serialization

```python
# pjt/settings.py
INSTALLED_APPS = [
    ...
	'api',
    'rest_framework'	# 등록
]



# api앱에 serializers.py 추가

# api/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    
    def create(self, validated_data):
        return Article.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
```

```bash
$ cd pjt

$ python manage.py shell
```

```shell
$ from api.models import Article

$ from api.serializers import ArticlesSerializer

$ from rest_framework.renderers import JSONRenderer

$ from rest_framework.parsers import JSONParser

$ a = Article(title = "article title", description = "this is description")

$ a.save
```

| ![3](DRF.assets/3.png) |
| :--------------------: |

```shell
serializer = ArticleSerializer(a)

serializer.data
('title': 'article title', 'description': 'this is description')

json = JSONRenderer().render(serializer.data)

json
b'("title": "article title", "description": "this is description")'

import io

stram = io.BytesIO(json)

data = JSONParser().parse(stream)

serializer = ArticleSerializer(data=data)

serializer.is_valid()
True

serializer.validated_data
OrderedDict([('title', 'article title'), ('description', 'this is description')])
```





### Model Serializer

 ```python
 # api/serializers.py
 
 # 기존
 class ArticleSerializer(serializers.Serializer):
     '''title = models.CharField(max_length=100)
     description = models.CharField(max_length=400)
     
     def create(self, validated_data):
         return Article.objects.create(validated_data)
     
     def update(self, instance, validated_data):
         instance.title = validated_data.get('title', instance.title)
         instance.description = validated_data.get('description', instance.description)'''
     
     
 # 변경
 class ArticleSerializer(serializers.ModelSerializer):
     class Meta:
         model = Article
         fields = ['id', 'title', 'description']        
 ```

```bash
$ python manage.py shell
```

```shell
from api.serializers import ArticleSerializer

serializer = ArticleSerializer()

print(repr(serializer))
ArticleSerializer():
	id = IntergerField(label='ID', read_onl=True)
	title = CharField(max_length=100)
	description = CharField(style={'base_template': 'textarea.html'})
```





### Function Based API View

```python
# api/views.py

from django.shortcuts import render, HttpResponse
from .models import Article	# 추가
from .serializers import ArticleSerializer	# 추가
from django.http import JsonResonse	# 추가
from rest_framework.parsers impoort JSONParser	# 추가
'''삭제
def Index(request):
    return HttpResponse("It is working")'''

def article_list(request):

    # get all articles
    if requset.method == 'GET':
        articles = Article.objects.all()
        serializer = Articleserializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    
elif request.method == 'POST':
    data = 
```





##### API View Decorator



##### Class Based API View



##### Mixins



##### ViewSets and Routers



##### Generic Viewset



##### Model Viewset



##### Authentication & Authorization



##### Registration