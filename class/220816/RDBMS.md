### RDBMS

- 관계형 데이터베이스 관리 시스템(RDBMS)

  - 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미
    - ex) MySQL, SQLite, PostgreSQL, ORACLE, SQL Server
  - SQLite
    - 서버 형태가 아닌 파일 형식으로 응용 프로그램에 넣어서 사용하는 비교적 가벼운 데이터베이스
    - 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨
    - 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능
  - SQLite Data Type
    1. NULL
    2. INTEGER
       - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호 있는 정수
    3.  REAL
       - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값
    4. TEXT
    5. BLOB
       - 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)

  - Sqlite Type Affinity : 특정 컬럼에 저장하도록 권장하는 데이터 타입
    1. INTEGER
    2. TEXT
    3. BLOB
    4. REAL
    5. NUMBERIC

![DB](C:\Users\dwde2\Pictures\KDT\DB.png)