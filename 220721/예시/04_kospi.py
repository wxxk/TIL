import requests

URL = 'https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page=1&pageSize=20'

response = requests.get(URL).json()
# print(response)
# print(response.get('stocks')[0]) #주식의 첫번째 값(삼성전자 주식 값)
print(response.get('stocks')[0].get('closePrice'))
