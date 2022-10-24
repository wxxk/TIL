# Django ModelForm

### 개요

- DB 기반의 어플리케이션을 개발하다보면, HTML Form(UI)은 Django모델(DB)과 밀접한 관계를 가지게 됨
  - 사용자로부터 값을 받아 DB에 저장하여 활용하기 때문
  - 즉, 모델에 정의한 필드의 구성 및 종류에 따라 HTML Form이 결정됨
- 사용자가 입력한 값이 DB의 데이터 형식와 일치하는지를 확인하는 `유효성 검증`이 반드시 필요하며 이는 `서버 사이드`에서 반드시 처리해야 함.



### ModelForm Class

- Model을 통해 `Form Class`를 만들 수 있는 helper class

- ModelForm은 Form과 똑같은 방식으로 View 함수에서 사용



### ModelForm 선언

- forms 라이브러리의 ModelForm 클래스를 상속받음
- 정의한 ModelForm 클래스 안에 Meta 클래스를 선언
- 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

```python
# articles/forms.py

from django import forms
from .model import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        moel = Article
        fields = '__all__'
        
        # Meta class
        ## ModelForm의 정보를 작성하는 곳
        ## ModelForm을 사용할 경우 참조 할 모델이 있어야 하는데, 
        ## Meta class의 model 속성이 이를 구성함
        ### 참조하는 모델에 정의된 field 정보를 Form에 적용함
		## fields 속성에 '__all__'를 사용하여 모델의 모든 필드를 포함할 수 있음
        ## 또는 exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 있음
	
    '''
    class Meta:
    	model = Article
    	exclude = ('title',)
	'''
```



### ModelForm 활용

```python
# 1. ModelForm 객체를 context로 전달

# articles/views.py

from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)
```

```html
<!-- 2. Input Field 활용 -->
<!-- articles/new.html -->
{% extends 'base.html' %}
{% block content %}
	<h1>NEW</h1>
	<form action="{% url 'articles:create' %}" method="POST">
		{% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
	</form>
	<hr>
	<a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```



# ModelForm with view functions

### ModelForm 활용 로직

- 요청 방식에 따른 분기
  - HTML Form 전달
  - 사용자 입력 데이터 수신
- 유효성 검사에 따른 분기
  - 유효성 검사 실패시 Form으로 전달
  - 유효성 검사 성공시 DB 저장



### CREATE

```python
# articles/views.py

def create(request):
    form = ArticleForm(request.POST)
    # 유효성 검사 통화하면
    if form.is_vaild():
        
        # 데이터 저장 후 
        article = form.save()
        
        # 상세 페이지 리다이렉트
        return redirect('articles:detail', article.pk)
    
    # 유효성검사 False인 경우 form 인스턴스에 errors 속성에 값이 작성되는데,
    # 유효성 검증을 실패한 원인이 딕셔너리 형태로 저장됨.
    print(f'에러: {form.errors}')
    
    # 통과목하면 작성페이지로 리다이렉트
    return redirect('articles:new')
```

- `is_vaild()` method
  - 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
  - 데이터 유효성 검사를 보장하기 위한 is_vaild()를 제공하여 개발자의 편의를 도움
- The `save()` method
  - form 인스턴스에 바인딩 된 데이터를 통해 데이터베이스 객체를 ㅈ만들고 저장
  - ModelForm의 하위 클래스는 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정함
    - 제공되지 않은 경우 save()는 지정된 모델의 새인스턴스를 만듦(CREATE)
    - 제공되면 save)는 해당 인스턴스를 수정(UPDATE)



### UPDATE

- ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를지정
- request.POST
  - 사용자가 form을 통해 전송한 데이터 (새로운 데이터)
- instance
  - 수정이 되는 대상



- edit - view 수정

```python
# articles/views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article':article,
        'form':form,
    }
    return render(request, 'articles/edit.html', context)
```

- edit - template 수정

```html
<!-- articles/edit.html -->
{% extends 'base.html' %}
{% block content %}
    <h1>EDIT</h1>
    <form action="{% url 'articles:update' article.pk %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}		<!-- 수정 -->
        <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```

- update - view 수정

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_vaild():
        form.save()
    	return redirect('articles:detail', article.pk)
    context = {
        'form':form
        'article':article,
    }
    return render(request, 'articles/edit.html', context)
```

---

### 실습

![1004](README.assets/1004.png)
