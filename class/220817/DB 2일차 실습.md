# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```



### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```



### table 및 스키마 조회

```sql
sqlite3> .tables
-- healthcare

sqlite3> .schema healthcare
-- CREATE TABLE healthcare (
--     id PRIMARY KEY,        
--     sido INTEGER NOT NULL, 
--     gender INTEGER NOT NULL,
--     age INTEGER NOT NULL,  
--     height INTEGER NOT NULL,
--     weight INTEGER NOT NULL,
--     waist REAL NOT NULL,   
--     va_left REAL NOT NULL, 
--     va_right REAL NOT NULL,

--     blood_pressure INTEGER 
--     NOT NULL,
--     smoking INTEGER NOT NULL,
--     is_drinking BOOLEAN NOT NULL
-- );
```



## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare;
```

```
count(*)
--------
1000000
```



### 2. 연령 코드 (age)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT max(age), min(age) FROM healthcare;
```

```
max(age)  min(age)
--------  --------
18        9
```



### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
SELECT max(height), min(height), max(weight), min(weight) FROM healthcare;
```

```
max(height)  min(height)  max(weight)  min(weight)
-----------  -----------  -----------  -----------
195          130          135          30
```



### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT count(*) FROM healthcare WHERE height BETWEEN 160 and 170;
```

```
count(*)
--------
516930
```



### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오.

```sql
SELECT * FROM healthcare WHERE is_drinking = 1 and waist != '' ORDER BY waist DESC LIMIT 5;

```

```
id      sido  gender  age  height  weight  waist  va_lftREAL  va_right  blood_e  smoking  is_drinking
------  ----  ------  ---  ------  ------  -----  ----------  --------  -------  -------  -----------
993531  48    1       9    170     130     146.0  0.6         0.8       150      3        1
87897   48    1       10   170     130     142.0  0.6         0.8       140      1        1
826643  48    1       9    180     135     141.4  1.2         0.9       136      3        1
567314  26    1       11   170     110     140.0  0.3         0.6       125      3        1
611146  36    1       12   165     120     140.0  0.4         0.8       141      3        1
```



### 6. 시력 양쪽(va_left, va_right)이 1.5 이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare WHERE (va_right >=1.5 and va_left >=1.5) and is_drinking = 1;
```

```
count(*)
--------
36697
```



### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare WHERE blood_pressure < 120;
```

```
count(*)
--------
360808
```



### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT avg(waist) FROM healthcare WHERE blood_pressure >= 140;
```

```
avg(waist)
----------------
85.8665098512525
```



### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
SELECT avg(height), avg(weight) FROM healthcare WHERE gender=1;
```

```
avg(height)       avg(weight)
----------------  ----------------
167.452735422145  69.7131620222875
```



### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;
```

```
id      height  weight
------  ------  ------
836005  195     110
```



### 11. BMI가 30이상인 사람의 수를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다.

> 키는 미터 단위로 계산한다.

```sql
SELECT COUNT(*) FROM healthcare WHERE weight*10000/(height*height) >= 30;
```

```
COUNT(*)
--------
53121
```



### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다.

> 키는 미터 단위로 계산한다.

```sql
SELECT id, weight*10000/(height*height) AS BMI FROM healthcare WHERE smoking = 3 ORDER BY weight*10000/(height*height) DESC LIMIT 5;
```

```
id      BMI
------  ---
231431  50
934714  49
722707  48
947281  47
948801  47
```



### 13. 나이가 10대인 사람들의 평균 키와 몸무게를 출력하시오.

```sql
-- LIKE
SELECT avg(height), avg(weight) FROM healthcare WHERE age LIKE '1_';

-- BETWEEN
SELECT avg(height), avg(weight) FROM healthcare WHERE age BETWEEN 10 and 19;
```

```
avg(height)       avg(weight)
----------------  ----------------
160.093282985056  62.2866628028393
```



### 14. 흡연이 1이고 음주가 0인 사람의 BMI지수를 낮은 순으로 5명 출력하시오.

```sql
SELECT *, weight*10000/(height*height) AS BMI FROM healthcare WHERE smoking = 1 and is_drinking = 0 ORDER BY weight*10000/(height*height) ASC LIMIT 5;
```

```
id      sido  gender  age  height  weight  waist  va_left  va_right  blood_pressure  smoking  is_drinking  BMI
------  ----  ------  ---  ------  ------  -----  -------  --------  --------------  -------  -----------  ---
758886  41    2       9    170     30      54.0   0.5      0.7       110             1        0            10
139543  44    2       11   160     30      55.0   1.2      0.6       110             1        0            11
268110  48    1       15   160     30      85.0   0.6      0.6       130             1        0            11
506264  43    1       17   160     30      59.0   0.4      0.4       133             1        0            11
775919  30    2       13   160     30      53.0   1.2      1.2       120             1        0            11
```



### 15. 왼쪽 눈이 2.0 이고 오른쪽 눈이 0.5이하이거나 오른쪽 눈이 2.0이고 왼쪽눈이 0.5이하인 사람을 COUNT 하라 (column이름은 wear_glasses)

```sql
SELECT count(*) FROM healthcare WHERE (va_left = 2.0 and va_right <= 0.5) or (va_right = 2.0 and va_left <= 0.5);
```

```
wear_glasses
------------
89
```

