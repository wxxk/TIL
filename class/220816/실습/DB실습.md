# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE age<10;
```

```
COUNT(*)
--------
156277
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE gender = 1;
```

```
COUNT(*)
--------
510689
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE smoking = 1 and is_drinking =1;
```

```
COUNT(*)
--------
287992
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 and va_right >= 2.0;
```

```
COUNT(*)
--------
2614
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
SELECT DISTINCT sido FROM healthcare;
```

```
sido
----
36
27
11
31
41
44
48
30
42
43
46
28
26
47
45
29
49
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> 예) 허리 둘레가 x이상이면서 몸무게가 y이하인 사람

ex1. 성별이 1인 10대인 사람의 수를 출력하시오.

```python
SELECT COUNT(*) FROM healthcare WHERE gender=1 and 10<=age<20;
COUNT(*)
--------
510689
```

ex2. 성별이 2면서 키 180이상인 사람의 수를 출력하시오. 

```python
SELECT COUNT(*) FROM healthcare WHERE gender=2 and height>=180;
COUNT(*)
--------
31
```

ex2-1. ex2 중 가장 큰 사람의 키를 출력하시오.

```python
SELECT height FROM healthcare WHERE gender=2 and height>=180 ORDER by height DESC LIMIT 1;
height
------
185
```



1. 허리 둘레가 80이상이면서 몸무게가 50이하인 사람 

```python
SELECT COUNT(*) FROM healthcare WHERE waist>=80 and weight<=50;
COUNT(*)
--------
26774
```

2. 키가 180이상인 사람 

```python
SELECT COUNT(*) FROM healthcare WHERE height>=180;
COUNT(*)
--------
28829
```

3. 키가 160이하인 사람 

```python
SELECT COUNT(*) FROM healthcare WHERE height<=180;
COUNT(*)
--------
995483
```

4. 흡연수치가 3이고, 음주가 0이면서, 혈압이 130 이상인 사람 

```python
SELECT COUNT(*) FROM healthcare WHERE smoking=3 and is_drinking=0 and blood_pressure>=130;
COUNT(*)
--------
11416
```

5. 흡연수치가 1이고, 음주가 0이면서, 혈압이 130 이상인 사람  

```python
SELECT COUNT(*) FROM healthcare WHERE smoking=1 and is_drinking=0 and blood_pressure>=130; 
COUNT(*)
--------
136895
```

6. 흡연수치가 1이고, 음주가 1이면서, 혈압이 130 이상인 사람

```python
SELECT COUNT(*) FROM healthcare WHERE smoking=1 and is_drinking=1 and blood_pressure>=130; 
COUNT(*)
--------
96364
```

