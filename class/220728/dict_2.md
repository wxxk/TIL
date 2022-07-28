### 딕셔너리 기본 문법

- 선언 : `변수 ={key1 : value1, key2: value2 ... }`

```python 
a = {
    "name": "kyle"
    "gender": "male"
    "address": "Seoul"
}
print(a).
# {'name': 'kyle', 'gender' : 'male', 'address' : 'Seoul'}
```



- 삽입 및 수정 : `딕셔너리[key] = value`
  - 내부의 해당 key가 없으면 삽입 / 있으면 수정

```python
a = {
    "name": "kyle"
    "gender": "male"
    "address": "Seoul"
}
a["job"] = "coach"
print(a)
# {'name': 'kyle', 'gender': 'male', 'addresss': 'Seoul', 'job': 'coach'} # 삽입

===============================================================================
a = {
    "name": "kyle"
    "gender": "male"
    "address": "Seoul"
}
a["name"] = "justin"
# print(a)
# {'name': 'justin', 'gender': 'male', 'addresss': 'Seoul'} # 수정
```



- 삭제 : `딕셔너리.pop(key)`

  - 내부에 존재하는 key에 대한 value 삭제 및 **반환**

  - 존재하지 않는 key에 대해서는 keyError 발생

- 삭제 : `딕셔너리.pop(key, default)`

  - 두 번째 인자로 default(기본)값을 지정하여 KeyError 방지 가능

```python
a = {
    "name": "kyle"
    "gender": "male"
    "address": "Seoul"
}
gender= a.pop("gender")

print(a)
print(gender)
# {'name': 'kyle', 'addrress': 'Seoul'}
# male

=========================================================================
a = {
    "name": "kyle"
    "gender": "male"
    "address": "Seoul"
}
gender= a.pop("phone")

print(a)
print(phone)
# KeyError

=========================================================================
a = {
    "name": "kyle"
    "gender": "male"
    "address": "Seoul"
}
phone = a.pop("phone", "010-1234-5678")

print(a)
print(phone)
# {'name': 'kyle', 'gender': 'male', 'address': 'Seoul'}
# 010-1234-5678
```



- 조회 : `딕셔너리[key]`
  - key에 해당하는 value 반환
- 조회 : `딕셔너리.get(key, default)`

```python
a = {
    "name": "kyle"
    "gender": "male"
    "address": "Seoul"
}
print(a["name"])
# kyle (key가 없으면 Error)

========================================================================
a = {
    "name": "kyle"
    "gender": "male"
    "address": "Seoul"
}
print(a.get("phone", "없음"))
# 없음 (key가 없으면 default)
```