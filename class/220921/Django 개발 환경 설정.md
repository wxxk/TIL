# Django 개발 환경 설정

```bash
$ mkdir server		# server 폴더 만들기

$ cd server/		# server 폴더로 이동

$ pip list			# 어떤 것이 깔려있는지 확인

$ python --version 	# python 버전 확인


# 개발 환경 (상대위치 중요!!!)
$ python -m venv server-venv		# python -m venv [가상환경이름]

$ source server-venv/Scripts/activate	# 가상환경 작동

$ deactivate	# 가상환경 종료

$ pip list		# django 설치 확인

$ pip install django==3.2.13	# djnago 3.2.13 버전 설치

$ pip list		# 설치된 것들 확인

$ django-admin startproject firstpjt .		# django-admin : 장고를 관리하는 애
# $ django-admin startproject [프로젝트이름] [시작경로]
# . : 현재 위치

$ code .		# VScode로 현재 폴더를 열기

$ python manage.py runserver		# manage.py 실행 / 웹 서버 실행

# 이후 주소창에 localhost:8000 -> django페이지가 보이면 웹 서버 구동 성공!!!
```







