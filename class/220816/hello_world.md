### 문법 정리

테이블 생성 및 삭제

- 데이터베이스 생성하기

```sqlite
$ sqlite3 tutorial.sqlite3
sqlite> .databes
```

- csv 파일을 table로 만들기

```sqlite
sqlite> .mode csv
sqlite> .import hellodb.csv examples
sqlite> . tables
examples
```

- SELECT

```sqlite
SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-0000-0000
-- SELECT 문은 특정 테이블의 레코드(행) 정보를 반환!
```

- (Optional) 터미널 view 변경하기

```sqlite
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-0000-0000
sqlite> .header on
sqlite> SELECT * FROM examples;
id,first_name,last_anem,age,country,phone
1,"길동","홍",600,"충청도",010-0000-0000
sqlite> .mode column
sqlite> SELECT * FROM examples;
id  first_name  last_name  age  country  phone
--  ----------  ---------  ---  -------  -------------
1   길동          홍          600  충청도      010-0000-0000
```

- CREATE

```sqlite
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY,
    name TEXT
);
```

- CREATE - 테이블 생성 및 확인하기

```python
sqlite> CREATE TABLE classmates (
	...> id INTEGER PRIMARY KEY,
    ...> name TEXT
    ...> );
-- sqlite> .tables
-- classmates examples
```

- 특정 테이블의 schema 조회

```sqlite
sqlite> .schema classmates
-- CREATE TABLE classmates (
-- id INTEGER PRIMARY KEY,
-- name TEXT
-- );
```

- DROP

```sqlite
sqlite> DROP TALBE classmates;
sqlite> .tables
-- examples
```

- 필드 제약 조건
  - NOT NULL : NULL 값 입력 금지
  - UNIQUE : 중복 값 입력 금지 (NULL 값은 중복 입력 가능)
  - PRIMARY KEY : 테이블에서 반드시 하나. NOT NULL + UNIQUE
  - FOREIGN KEY : 외래키. 다른 테이블의 KEY
  - CHECK : 조건으로 설정된 값만 입력 허용
  - DEFAULT : 기본 설정 값

