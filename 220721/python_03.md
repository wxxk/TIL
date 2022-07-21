#### 가상 환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야됨
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
  - 과거 외주 프로젝트 - django 버전 2.x
  - 신규 회사 프로젝트 - django 버전 3.x
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리 할 수 있음

##### 파이썬 실행에 대한 이해

- python은 특정 경로에 있는 프로그램을 실행시키는 것

##### venv

- 가상 환경을 만들고 관리하는데 사용되는 모듈(Python 버전 3.5부터)
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
  - 특정 폴더에 가상 환경이(패키지 집합 폴더 등)  있고
  - 실행 환경(예 - bash)에서 가상환경을 활성화 시켜
  - 해당 폴더에 있는 패키지를 관리/사용함

##### 가상환경 생성

- 가상환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨

  `$ python -m venv <폴더명>`

##### 가상환경 활용

- 아래의 명령어를 통해 가상환경을 활성화

  - <venv>는 가상환경을 포함하는 디렉토리 이름

  | 플랫폼 | 셀              | 가상 환경을 활성화하는 명령           |
  | ------ | --------------- | ------------------------------------- |
  | POSIX  | bash / zsh      | $ source <venv> /bin /activate        |
  |        | fish            | $ source <venv> /bin /activate.fish   |
  |        | csh / tcsh      | $ source <venv> /bin /activate.csh    |
  |        | PowerShell Core | $ <venv> /bin /Activate.ps1           |
  | 윈도우 | cmd.exe         | C:\> <venv> \Scripts \activate.bat    |
  |        | PowerShell      | PS C:\> <venv> \Scripts \Activate.ps1 |

  - 가상환경 비활성화는 $ deactivate 명령어를 사용

##### cmd와 bash 환경

- 가상환경 활성화/비활성화

  `$ source venv/Scripts/activate`