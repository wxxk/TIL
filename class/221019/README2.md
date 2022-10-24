# 1:N

### 1. User - Comment



### 2. CREATE

---

### 1. User - Comment

- 관계 모델 설정

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

- Migration 진행

```git
$ python manage.py makemigrations

$ python manage.py migrate
```





---

### 2. CREATE

- CommentForm의 출력 필드 수정

```python
# articles/forms.py

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        exclude = ('article', 'user',)
```

- save의 commit 옵션 활용

```python
# articles/views.py

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)
```





---

### 3. DELETE

- 댓글 삭제 시 작성자 확인

```python
# articles/views.py

def comments_delete(reqeust, articles_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', articles_pk)
```

- 추가로 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 함

```html
{% if request.user == comment.user %}
	<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
		{% csrf_token %}
		<input type="submit" value="DELETE">
	</form>
{% endif %}
```

