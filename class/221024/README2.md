# M:N

### Django ManyToManyField

- Django ManyToManyField 작성
- Migration
- URL, Views, HTML





---

### Django ManyToManyField

- Django ManyToManyField 작성

```python
# models.py

class Article(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```

- Migration

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- URL, Views, HTML

```python
# articles/urls.py

app_name = 'articles'

urlpatterns = [
	...
    path('<int:pk>/like', views.liek, name='like')
]



# articles/views.py

def like(request, pk):
    article = Article.objects.get(pk=pk)
    # 좋아요 취소
    # if article.like_users.filter(id=request.user.id).exists()
    if request.user in article.like_users.all():
	    article.like_users.remove(request.user)
    # 좋아요
	else:
    	article.like_users.add(requset.user)
    return redirect('articles:detail', pk)
```

```html
<!-- html -->

{% if request.user.is_authenticated %}
    <!-- 좋아요 버튼 -->
    <a href="{% url 'articles:like' article.pk %}">
    {% if request.user in article.like_user.all %}
        좋아요 취소
    {% else %}
        좋아요
    {% endif %}
        </a>
{% endif %}
<!-- 좋아요 개수 -->
{{ article.like_users.count }}
```

