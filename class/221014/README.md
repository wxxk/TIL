# Django Pair Project 3

### 20221014 KDT - 실무 맞춤형 풀스택 1기 1회차 이상욱 @wxxk

>- 회원가입, 로그인, 회원 목록 조회, 회원 정보 조회, 회원 정보 수정, 로그아웃

### 목차

| 내용                            |
| ------------------------------- |
| [프로젝트소개](#프로젝트소개) |
| [코드구현](#코드구현)           |
| [코드실행](#코드실행)           |
| [배운점](#배운점)             |



### 프로젝트소개

---

- #### 목적

  >페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스 개발
  >
  >- CRUD 구현
  >- Staticfiles 활용 정적 파일(이미지, CSS, JS) 다루기
  >- Django Auth 활용 회원 관리(회원가입 / 회원조회 / 로그인 / 로그아웃)



- #### 개발 환경

  > 언어 : HTML, CSS, Python, JavaScript
  >
  > 프레임워크 : Django



### 코드구현

---

> ### 1. 회원가입
>
> >앱 App
> >
> >앱 이름 : accounts
> >
> >모델 Model
> >
> >모델 이름 : User
>
> - Django **AbstractUser** 모델 상속
>
> **폼 Form**
>
> - Django 내장 회원가입 폼 UserCreationForm을 상속 받아서 CustomUserCreationForm 작성
> - 해당 폼은 아래 필드만 출력합니다.
>   - username
>   - first_name
>   - last_name
>   - password1
>   - password2
>   - email
>
> **기능 View**
>
> - 회원가입	
>
>   - `POST` http://127.0.0.1:8000/accounts/signup/
>
>   - CustomUserCreationForm을 활용해서 회원가입 구현
>
> **화면 Template**
>
> - 회원가입 페이지
>
>   - `GET` http://127.0.0.1:8000/accounts/signup/
>
>   - 회원가입 폼
>
> 
>
> ------
>
> ### 2. 로그인
>
> **폼 Form**
>
> - 로그인
>   - Django 내장 로그인 폼 **AuthenticationForm 활용**
>
> **기능 View**
>
> - 로그인
>
>   - `POST` http://127.0.0.1:8000/accounts/login/
>
>   - **AuthenticationForm**를 활용해서 로그인 구현
>
> **화면 Template**
>
> - 로그인 페이지
>
>   - `GET` http://127.0.0.1:8000/accounts/login/
>
>   - 로그인 폼
>
>   - 회원가입 페이지 이동 버튼
>
> 
>
> ------
>
> ### 3. 회원 목록 조회
>
> **기능 View**
>
> - 회원 목록 조회
>   - `GET` http://127.0.0.1:8000/accounts/
>   - is_superuser를 활용해서 관리자만 볼 수 있도록 구현
>
> **화면 Template**
>
> - 회원 목록 페이지
>
>   - `GET` http://127.0.0.1:8000/accounts/
>
>   - 회원 목록 출력
>
>   - 회원 아이디를 클릭하면 해당 회원 조회 페이지로 이동
>
> 
>
> ------
>
> ### 4. 회원 정보 조회(admin)
>
> **기능 View**
>
> - 회원 정보 조회
>   - `GET` http://127.0.0.1:8000/accounts/int:user_pk/detail
>   - is_superuser를 활용해서 관리자만 볼 수 있도록 구현
>
> **화면 Template**
>
> - 회원 조회 페이지(프로필 페이지)
>
>   - `GET` http://127.0.0.1:8000/accounts/int:user_pk/detail
>
>     
>
> ---
>
> ### 5. 회원 정보 조회(사용자)
>
> **기능 View**
>
> - 회원 정보 조회
>   - `GET` http://127.0.0.1:8000/accounts/profile/
>
> **화면 Template**
>
> - 회원 조회 페이지(프로필 페이지)
>   - `GET` http://127.0.0.1:8000/accounts/profile/
>
> 
>
> 
>
> ------
>
> ### 7. 회원 정보 수정
>
> **폼 Form**
>
> - 회원 정보 수정
>   - Django 내장 회원 수정 폼 UserChangeForm을 상속 받아서 **CustomUserChangeForm** 작성
>   - 해당 폼은 아래 필드만 출력합니다.
>     - username
>     - email
>
> **기능 View**
>
> 회원 정보 수정
>
> - `POST` http://127.0.0.1:8000/accounts/update/
>
> **화면 Template**
>
> 회원 정보 수정 페이지
>
> - `GET` http://127.0.0.1:8000/accounts/update/
>
> 
>
> ------
>
> ### 8. 로그아웃
>
> **기능 View**
>
> - 로그아웃
>
>   - **AuthenticationForm**를 활용해서 로그아웃 구현
>
>   - `POST` http://127.0.0.1:8000/accounts/logout/
>
> 
>
> ------
>
> ### 9. 네비게이션바
>
> **화면 Template**
>
> - **네비게이션바**
>
>   - 리뷰 목록 페이지 이동 버튼
>
>   - 리뷰 작성 페이지 이동 버튼
>
>   - 비로그인 유저는 작성 버튼 클릭시 로그인 화면으로 이동
>
>   - 로그인 상태에 따라 다른 화면 출력
>     1. 로그인 상태
>        - 로그인 한 사용자의 username 출력
>          - 회원정보를 클릭하면 회원 정보 조회(사용자) 페이지로 이동
>          - 로그아웃 버튼
>     2. 비 로그인 상태
>        - 로그인 페이지 이동 버튼
>        - 회원가입 페이지 이동 버튼
>
> 
>
> ------
>
> ### 10. 리뷰 생성
>
> **앱 App**
>
> 앱 이름 : reviews
>
> 모델 Model
>
> 모델 이름 : Review
>
> - 모델 필드
>
>   | 이름       | 역할          | 필드     | 속성              |
>   | ---------- | ------------- | -------- | ----------------- |
>   | title      | 리뷰 제목     |          |                   |
>   | content    | 리뷰 내용     |          |                   |
>   | movie_name | 영화 이름     |          |                   |
>   | grade      | 영화 평점     |          |                   |
>   | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
>   | updated_at | 리뷰 수정시간 | DateTime | auto_now = True   |
>
> **기능 View**
>
> 데이터 생성
>
> - `POST` http://127.0.0.1:8000/reviews/create/
>
> **화면 Template**
>
> **리뷰 작성 페이지**
>
> - `GET` http://127.0.0.1:8000/reviews/create/
> - 리뷰 작성 폼
>
> 
>
> ------
>
> ### 11. 리뷰 목록 조회
>
> **기능 View**
>
> - 데이터 목록 조회
>   - `POST` http://127.0.0.1:8000/reviews/
>
> **화면 Template**
>
> - 리뷰 **목록 페이지**
>
>   - `GET` http://127.0.0.1:8000/reviews/
>
>   - 리뷰 목록 출력
>
>   - 더보기 버튼을 클릭하면 해당 리뷰의 정보 페이지로 이동
>
> 
>
> ------
>
> ### 12. 리뷰 정보 조회
>
> **기능 View**
>
> - 데이터 정보 조회
>   - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/
>
> **화면 Template**
>
> - **리뷰 정보 페이지**
>
>   - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/
>
>   - 해당 리뷰 정보 출력
>
>   - 수정 / 삭제 / 뒤로가기 버튼 
>
> 
>
> ------
>
> ### 13. 리뷰 정보 수정
>
> **기능 View**
>
> - 데이터 수정
>   - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
>
> **화면 Template**
>
> - **리뷰 수정 페이지**
>
>   - `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
>
>   - 리뷰 수정 폼
>   - 뒤로가기 버튼
>
> 
>
> ------
>
> ### 14. 리뷰 삭제
>
> **기능 View**
>
> - 데이터 삭제
>   - `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/delete/



### 코드실행

---

![ezgif.com-gif-maker](README.assets/ezgif.com-gif-maker.gif)

### 배운점

---

- `createsuperuser`와 `is_superuser`를 이용해 관리자만 볼 수 있는 페이지 만들기

  ```bash
  $ python manage.py createsuperuser
  사용자 이름: admin
  이메일 주소: admin@gmail.com
  Password:
  Password (again):
  비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
  비밀번호가 너무 일상적인 단어입니다.
  비밀번호가 전부 숫자로 되어 있습니다.
  Bypass password validation and create user anyway? [y/N]: y
  Superuser created successfully.
  (venv)
  ```

  ```python
  # views.py
  def index(request):
      if request.user.is_superuser:
          users = User.objects.all()
          context = {"users": users}
          return render(request, "accounts/index.html", context)
      else:
          return redirect("reviews:index")
  ```

  

- `CharField`에서 `choices`활용하기

  ```python
  # models.py
  
  # star_grade를 튜플로 정의
  class Review(models.Model):
    star_grade = (
      ('1','★'),
      ('2','★★'),
      ('3','★★★'),
      ('4','★★★★'),
      ('5','★★★★★'),
    )
  	grade = models.CharField(max_length=1, choices=star_grade)
  ```

  ![제목 없음](django_pjt_3.assets/제목 없음.png)

  - `choices`에 `start_grade`가 튜플로 정의

  ```html
  <!-- detail.html -->
  
  <!-- templates에서 별이 나오도록 표현 -->
  <h4 class="card-text">점수 : {{ review.get_grade_display }}</h4>
  ```

  
