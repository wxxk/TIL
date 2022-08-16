### CRUD

##### CREATE

- INSERT

  - "insert a single row into a table"

  - 테이블에 단일 행 삽입

    ```sqlite
    INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
    ```

  - 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력

    ```sqlite
    INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);
    ```

  - ex) 이름 홍길동, 나이 23

    ```sqlite
    INSERT INTO classmates (name, age) VALUES ('홍길동', 23)
    ```

  - ex) 이름 홍길동, 나이 30, 주소 서울

    ```sqlite
    INSERT INTO classmates VALUES ('홍길동', 30, '서울');
    -- name  age  address
    -- ----  ---  -------
    -- 홍길동   23
    -- 홍길동   23   서울
    ```

  - rowid : SQLite에서 PRIMARY KEY가 없는 경우 자동으로 증가하는 PK 컬럼

    ```sqlite
    sqlite> SELECT rowid, * FROM classmates;
    -- rowid  name  age  address
    -- -----  ----  ---  -------
    -- 1      홍길동   23
    -- 2      홍길동   23   서울
    ```

  - 비어 있는 주소

    ```sqlite
    sqlite> SELECT * FROM classmates;
    -- name  age  address
    -- ----  ---  -------
    -- 홍길동   23
    -- 홍길동   23   서울
    ```

  - 지우고 새로 만들기

    ```sqlite
    sqlite> DROP TALBE classmates;
    sqlite> CREATE TABLE classmates (
    	id INTEGER PRIMARY KEY,
       	name TEXT NOT NULL,
        age INT NOT NULL,
        address TEXT NOT NULL
    );
    ```

    

##### READ

- SELECT
  - 테이블에서 데이터를 조회
  - SELECT문은 SQLite에서 가장 기본이 되는 문이며, 다양한 절(clause)과 함께 사용
    - ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY etc...

- LIMIT
  - "constrain the number of rows returned by a query"
  - 쿼리에서 반환되는 행 수를 제한
  - 특정 행부터 시작해서 조회하기 위해 `OFFSET` 키워드와 함께 사용하기도 함
- WHERE
  - "specify the search condition for rows returned by the query"
  - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
- SELECT DISTINCT
  - "remove duplicate rows in the result set"
  - 조회 결과에서 중복 행을 제거
  - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함

- OFFSET : 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형

  - 예시:

    1. 문자열 'abcedf'에서 문자 'c'는 시작점 'a'에서 2의 OFFSET을 지님

    2. SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5

       - "6번째 행부터 10개 행을 조회 (6번째 행부터 10개를 출력)"
       - 0부터 시작함

       

- id, name 컬럼 값만 조회

  ```sqlite
  SELECT rowid, name FROM classmates;
  -- rowid  name
  -- -----  ----
  -- 1      홍길동  
  -- 2      김철수
  -- 3      이호영
  -- 4      박민희
  -- 5      최혜영
  ```

- id, name 컬럼 값을 하나만 조회 `LIMIT`

  ```sqlite
  SELECT rowid, name FROM classmates LIMIT 1;
  -- rowid  name
  -- -----  ----
  -- 1      홍길동  
  ```

- classmates 테이블에서 id, name 컬럼 값을 세 번째에 있는 하나만 조회

  ```sqlite
  SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
  -- rowid  name
  -- -----  ----
  -- 3      이호영
  ```

- classmates 테이블에서 age값 전체를 중복없이 조회

  ```sqlite
  SELECT DISTINCT age FROM classmates;
  -- age
  -- ---
  -- 30
  -- 26
  -- 29
  -- 28
  ```

  

##### UPDATE

- 수정

  - `rowid`로 했을 경우
    - 삭제하고 추가했을 때 번호가 이어짐
  - `PRIMARY KET AUTOINCREMENT`로 했을 경우
    - 삭제하고 추가했을 때 번호가 삭제된 값을 건너띄고 생성

  ```sqlite
  UPDATE classmates SET address='서울' WHERE rowid=5
  -- rowid name  age  address
  -- ----- ----  ---  -------
  -- 1 홍길동   30   서울
  -- 2 김철수   30   제주
  -- 3 이호영   26   인천
  -- 4 박민희   29   대구
  -- 5 이상욱   27   서울
  ```

  

##### DELETE

- 삭제(하나의 코드만 삭제)

  - DROP은 테이블 자체를 삭제

  ```sqlite
  DELETE FROM classmates WHERE rowid = 5;
  -- name  age  address
  -- ----  ---  -------
  -- 홍길동   30   서울
  -- 김철수   30   제주
  -- 이호영   26   인천
  -- 박민희   29   대구
  ```

