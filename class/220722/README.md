# 프로젝트 02

### API를 사용하기 전에 확인해야 할 것?

>정보 주고 받을 때 활용(Application Programming Interface : 응용 프로그램 인터페이스) ,

컴퓨터와 컴퓨터 프로그램 사이의 연결

- 요청하는 방식에 대한 이해
  - 인증 방식
  - URL 생성
    - 기본 주소
    - 원하는 기능에 대한 추가 경로
    - 요청 변수(필수와 선택)
- 응답 결과에 대한 이해
  - 응답 결과 타입(JSON)
  - 응답 결과 구조



### API 예시

```python
# pip install requests 
import requests   #import : 모듈 불러오기

# URL로
order_currency = 'BTC' 
payment_currency = 'KRW' 
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

# 요청을 보내고
response = requests.get(URL)   #get() : 딕셔너리 가져오기

# 응답 받은 값을 가져옴
print(response, type(response)) # <Response [200]> <class 'requests.models.Response'>

# 속성 예시
print(response.status_code) # 200 
print(response.text, type(response.text)) # 문자열

# 메서드 예시
# .json() 텍스트 형식의 JSON 파일을 파이썬 데이터 타입으로 변경!
print(response.json(), type(response.json())) #  <class 'dict'>

data = response.json()
# data는 딕셔너리 => key로 접근
print(data.get('data').get('closing_price'))
```

#### requests 모듈

```python
# 랜덤 이름, 나이
# https://api.agify.io?name=michael
import requests

URL = 'https://api.agify.io'
params = {
    'name': 'eunbin'
}
response = requests.get(URL, params=params).json()
print(response)
```

