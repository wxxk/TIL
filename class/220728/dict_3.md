### 딕셔너리 메서드

- `.keys()` : 딕셔너리의 key 목록이 담긴 dict_keys 객체 반환

```python
a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}

print(a.keys())
# dict_keys(['name', 'gender', 'address'])

for key in a.keys():
    print(key)
# name
# gender
# address

for key in a:
    print(key)
# name
# gender
# address
```



- `.values()` : 딕셔너리의 value 목록이 담긴 dict_values 객체 반환

```python
a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}

print(a.values())
# dict_values(['kyle', 'male', 'Seoul'])
      
for value in a.values():
    print(value)
# kyle
# male
# Seoul
```



- `.items()` : 딕셔너리의 (key, value) 쌍 목록이 담긴 dict_items 객체 반환

```python
a = {
    "name": "kyle",
    "gender": "male",
    "address": "Seoul"
}

print(a.item())
# dict_items([('name', 'kyle'), ('gender', 'male'), ('address', 'Seoul')])

for item in a.items():
    print(item)
# ('name, 'kyle')
# ('gender', 'male')
# ('address', 'Seoul')

for key, value in a.item():
    print(key, value)
# name kyle
# gender male
# address Seoul
```