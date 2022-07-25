import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r. status_code