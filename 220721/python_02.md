### 파이썬 버전별 업데이트

####  묘듈 심화

##### 파이썬 표준 라이브러리(PSL)

- 파이썬에 기본적으로 설치된 모듈과 내장함수
  - https://docs.python.org/ko/3/library/index.html
- 파이썬에 기본적으로 설치된 모듈과 내장 함수
  - 예시 = random.py

##### 파이썬 패키지 관리자(pip)

- PyPi(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리시스템

##### 파이썬 패키지 관리자 명령어

> **모두 bash, cmd 환경에서 사용되는 명령어**

- 패키지 설치

  - 최신 버전/ 특정 버전/ 최소 버전을 명시하여 설치 할 수 있음

  - 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음

    `$ pip install SomePackage`

    `$ pip install SomePackage==1.0.5`

    `$ pip install SomePackage=>1.0.4`

    > 모두 bash, cmd 환경에서 사용되는 명령어

- 패키지 삭제

  - pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌

    `$ pip uninstall SomePackage`

  - 패키지 목록 및 특정 패키지 정보

    `$ pip list`

    `$ pip show SomePackage`

- 패키지 freeze

  - 설치된 패키지의 비슷한 목록을 만들지만, pip install에서 활용되는 형식으로 출력

  - 해당하는 목록을 requirements.txt(관습)으로 만들어 관리함

    `$ pip fressze`

- 패키지 관리하기

  - 아래의 명령어들을 통해 패키지 목록을 관리[1]하고 설치할 수 있음[2]

  - 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함

    `$ pip freeze > requirements.txt`

    `$ pip install -r requirements.txt`

- 다양한 파이썬 프로젝트에서 사용됨

