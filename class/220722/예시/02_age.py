# https://api.agify.io?name=michael

from cgitb import reset
from urllib import response
import requests

URL = 'https://api.agify.io'
params = {
    'name': 'sangwook'
}
response =requests.get(URL, params=params).json()
print(response)