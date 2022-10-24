# Django Auth

### 0. 사전설정

- accounts app 생성 및 등록
- url 분리 및 매핑
- User model 활용하기



### 1. 회원가입

- UserCreationForm() 커스텀하기
- URL / Views / html 작성
- 회원가입 링크 작성



### 2. 로그인

- URL, Views, HTML
- 로그인 링크 작성



### 3. 로그아웃

- URL, Views, HTML
- 로그인 링크 작성



### 4. 회원정보 수정

- Form 정의
- URL, Views, HTML
- 회원정보 수정 링크 작성



### 5. 비밀번호 변경

- URL, Views, HTML



### 6. DELETE

---



### 0. 사전설정

- accounts app 생성 및 등록

```git
$ python manage.py startapp accounts
```

```python
# settings.py

INSTALLED_APPS = [
    'accounts',
]

# urls.py
urlpatterns = [
    path('accounts/', include('accounts.urls')),
]
```

- url 분리 및 매핑

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    
]
```

- User model 활용하기

```python
# settings.py
AUTH_USER_MODEL = 'accounts.User'

# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```



---

### 1. 회원가입

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]


# accounts/views.py
from django.contrib.auth.forms import CustomUserCreationForm

def signup(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # form.save()
            
            # 회원가입 이후 로그인
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
	else:
		form = CustomUserCreationForm()
	context = {
		'form': form,
	}
	return render(request, 'accounts/signup.html', context)
```

```html
<!-- accounts/signup.html -->
{% extends 'base.html' %}

{% block content %}
<h1>회원가입</h1>
<form action="{% url 'accounts:signup' %}" method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input type="submit">
</form>
{% endblock content %}
```

- 회원가입 링크 작성

```python
<!-- base.html -->

<a href="{% url 'accounts:signup' %}">Signup</a>
```

- UserCreationForm() 커스텀하기

```python
# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationFrom

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = "__all__" 
        # fields 임의로 선택
```





---

### 로그인

- URL, Views, HTML

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    ...
    path('login/', views.login, name='login')
]


# accounts/views.py
from django.contrib.auth import login as auth_login

def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			auth_login(request, form.get_user())
			return redirect('articles:index')
	else:
		form = AuthenticationForm()
	context = {
		'form': form
	}
	return render(request, 'accounts/login.html', context
```

```html
<!-- accounts/login.html -->
{% extends 'base.html' %}

{% block content %}
<h1>로그인</h1>
	<form action="{% url 'accounts:login' %}" method="POST">
		{% csrf_token %}
		{{ form.as_p }}
		<input type="submit">
	</form>
{% endblock content %}
```

- 로그인 링크 작성

```html
!-- base.html -->
<body>
    <div class="container">
        <a href="{% url 'accounts:login' %}">Login</a>
        <hr>
        {% block content %}
        {% endblock content %}
    </div>
</body>
```





---

### 3. 로그아웃

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	...
	path('logout/', views.logout, name='logout'),
]


# accounts/views.py

from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

```html
<!-- html -->

<!-- 로그아웃 form -->
<form action="{% url 'accounts:logout' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="Logout">
</form>
```





---

### 4. 회원정보 수정

```python
# accounts/forms.py

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChagneForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        
        
# accounts/views.py
from .forms import CustomUserChangeForm

def update(request):
	if request.method == 'POST':
		form = CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
	else:
		form = CustomUserChangeForm(instance=request.user)
	context = {
		'form': form,
	}
	return render(request, 'accounts/update.html', context)
```

```html
<!-- accounts/update.html -->

<form action="{% url 'accounts:update' %}" method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input type="submit">
</form>
```

- 회원정보 수정 페이지 링크 작성

```html
<a href="{% url 'accounts:update' %}">회원정보 수정</a>
```





---

### 5. 비밀번호 변경

- URL, Views, HTML

```python
# accounts/urls.py
app_name = 'accounts'

urlpatterns = [
	...,
	path('password/', views.change_password, name='change_password'),
]


# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            
            # 암호 변경 시 세션 무효화 방지
            update_session_auth_hash(requset, form.user)
            return redirect('articles:index')
	else:
		form = PasswordChangeForm(request.user)
	context = {
		'form': form,
	}
	return render(request, 'accounts/change_password.html', context)
```

```html
<!-- accounts/change_password.html -->

<form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
```





---

##### is_authenticated

- 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정

```html
<!-- html -->
{% if request.user.is_authenticated %}
```

```python
# views.py
def login(requset):
    if request.user.is_authenticated:
        return redirect('articles:index')
```



##### login_required

```python
from django.contrib.auth.decorators import login_required

@login_required
```

- "next" query string parameter 대응

```python
# accounts/views.py

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # request.GET.get('next')
            return redirect(reqeust.GET.get('next') or 'articles:index')
```

- 주의사항
  - login 템플릿에서 form action이 작성되어 있다면 동작하지 않음

```html
<!-- accounts/login.html -->

<form action="{% url 'accounts:login' %}" method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<input type="submit">
</form>
```





---

### 6. DELETE

```python
# accounts/views.py

def delete(request):
    request.user.delete()
    auth_logout(request)
    redirect('articles:index')
```



