### 문자열 메서드

> BOJ_17249 태보태보 총난타

- `.split(기준문자)`
  - 문자열을 일정 기준으로 나누어 리스트로 반환
  - 괄호 안에 아무것도 넣지 않으면 자동으로 고백을 기준으로 설정

```python
word = "I play the piano"
print(word.split()) # ['I', 'play', 'the', 'piano']
=====================================================
word = "apple,banana,orange,grape"
print(word.split(",")) #['apple', 'banana', 'oragne', 'grape']
=====================================================
word = "This_is_snake_case"
print(word.split("_")) #['This', 'is', 'snake', 'case']
```

- `.strip(제거할 문자)`
  - 문자열의 양쪽 끝에 있는 특정 문자를 모두 제거한 새로운 문자열 반환
  - 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 제거 문자로 설정
  - 제거할 문자를 여러 개 넣으면 해당하는 모든 문자들을 제거

```python
word = " Hello World"
print(word.strip()) #Hello World
===================================================
word = "aHello Worlda"
print(word.strip("a")) #Hello World
===================================================
word = "Hello World"
print(word.strip("Hd")) #ello Worl
===================================================
word = "Hello Wolrddddddddd"
print(word.strip("d")) #Hello worl
```

- `find(찾는 문자)`
  - 특정 문자가 처음으로 나타나는 **위치(인덱스)**를 반환
  - 찾는 문자가 없다면 -1을 반환

```python
word = "apple"
print(word.find("p")) #1
==================================================
word = "apple"
print(word.find("k")) #-1
```

- `.index(찾는 문자)`
  - 특정 문자가 처음으로 나타나는 **위치(인덱스)**를 반환
  - 찾는 문자가 없다면 오류 발생

```python
word = "apple"
print(word.index("p")) #1
=================================================
word = "apple"
print(word.find("k")) #ValueError: substring not
```

- `.count(개수를 셀 문자)`
  - 문자열에서 특정 문자가 몇 개인지 반환
  - 문자 뿐만 아니라, 문자열의 개수도 확인 가능

```python
word = "banana"
print(word.count("a")) #3
================================================
word = "banana"
print(word.count("na")) #2
================================================
word = "banana"
print(word.count("ana")) #1
```

- `삽입할 문자.join(iterable)`
  - iterable의 **각각 원소 사이에 특정 문자를 삽입**한 새로운 문자열 반환
  - 공백 출력, 콤마 출력 등 원하는 출력 형태를 위해 사용

```python
word = "happyhacking"
print(" ".join(word)) #h a p p y h a c k i n g
================================================
word = "happyhacking"
print(",".join(word)) #h,a,p,p,y,h,a,c,k,i,n,g
================================================
word = ["edu", "hphk.kr"]
print("@".join(word)) #edu@hphk.kr
================================================
words = ["h", "a", "p", "p", "y"]
print("".join(word)) #happy
```

