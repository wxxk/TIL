import requests

order_currency = 'BTC'
payment_cuurency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_cuurency}'
# 요청을 보내서
response = requests.get(URL)
# 응답 받을 값을 가져온다.
print(response, type(response)) # <Response [200]> <class 'requests.models.response'>

# 속성예시
print(response.status_code) # 200
print(response.text, type(response.text))

# 메서드 예시
# .json() 텍스트 형식의 JSON파일을 파이썬 데이터 타입으로 변경!
print(response.json())

print('=======================================')
# data는 딕셔너리 => key로 접근해요.

print(data.get('data').get('closing_price'))