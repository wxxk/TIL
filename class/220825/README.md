### QuertSet API

- gt(greater than) - 초과

  ```sql
  Entry.objcts.filter(id__gt=4)
  # filter(id > 4) <- 이러한 문법은 존재하지 않음
  
  # 대응하는 sql문
  SELECT ... WEHRE id > 4
  ```

- gte(greater the equal) -이상

  ```sql
  Entry.objcts.filter(id__gte=4)
  
  SELECT ... WEHRE id >= 4
  ```

- lt(less than) - 미만

  ```sql
  Entry.objcts.filter(id__lt=4)
  
  SELECT ... WEHRE id < 4
  ```

- lte(less than equal) - 이하

  ```sql
  Entry.objcts.filter(id__lt=4)
  
  SELECT ... WEHRE id < 4=
  ```

- in

  ```sql
  Entry.objects.filter(id__in=[1, 3, 4])
  Entry.objects.filter(headline__in='abc')
  
  SELECT ... WHERE id IN (1, 3, 4);
  SELECT ... WHERE headline IN ('a', 'b', 'c');
  ```

- startswith

  ```sql
  # Lennon으로 시작하는지
  Entry.objects.filter(headline__startswith='Lennon')
  
  SELECt ... WHERE headline LIKE 'Lennon%'
  ```

- istartswith

  ```sql
  # 대소문자 구분안함
  Entry.objects.filter(headline__istartswith='Lennon')
  
  SELECT ... WHERE headline ILIKE 'Lnnon%';
  ```

- endswith

  ```sql
  Entry.objects.filter(headline__endswith='Lennon')
  Entry.objects.filter(headline__iendswith='Lennon')
  
  SELECT ... WHERE headline LIKE '%Lennon';
  SELECT ... WHERE headline ILIKE '%Lennon';
  ```

- contanins

  ```sql
  Entry.objects.get(headline__contains='Lennon')
  Entry.objects.get(headline__icontains='Lennon')
  
  SELECT ... WHERE headline LIKE '%Lennon%';
  SELECT ... WHERE headline ILIKE '%Lennon%';
  ```

- range

  ```sql
  import datetime
  start_date = datetime.date(2005, 1, 1)
  end_date = datetime.date(2005, 3, 31)
  Entrty.objects.filter(pub_date__range(start_date, end_date))
  
  SELECT ... WHERE pub_date
  BETWEEN '2005-01-01' and '2005-03-31';
  ```

- 복합 활용

  ```sql
  inner_qs = Blog.objects.filter(name__contains='Cheddar')
  entries = Entry.objects.filter(blog__in=inner_qs)
  
  SELECT ...
  WHERE blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%cheddar%')
  ```

- 활용

  ```sql
  Entry.objects.all()[0]
  
  SELECT ...
  LIMIT 1;
  ```

  ```sql
  # 정렬
  Entry.objects.order_by('id')
  
  SELECT ...
  ORDER BY id;
  ---------------------------------------
  Entry.objects.order_by('-id')
  
  SELECT ...
  ORDER BY id DESC;
  ```

  

### ORM

- 모델링

  ```python
  class Genre(modes.Model):
      name = models.CharField(max_length=30)
     
  class Artist(models.Model):
      name = models.CharField(max_length=30)
  	debut = models.dateField()
      
  class Album(models.Model):
      name = models.CharField(max_length=30)
      genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
      artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
  ```

- models.ForeignKey 필드
  - 2개의 필수 위치 인자
    - Model class : 참조하는 모델
    - on_delete : 오래 키가 참조하는 객체가 삭제되었을 때 처리 방식
      - CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
      - PROTECT : 삭제되지 않음
      - SET_NULL : NULL 설정
      - SET_DEFAULT : 기본 값 설정

- Foreign Key (외래키)
  - 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
    - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
  - 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함



- 참조와 역참조

  ```sql
  # 1. 참조
  album - Album.objects.get(id=1)
  album.artist
  album.genre
  
  # 2. 역참조
  genre = Genre.objects.get(id=1)
  genre.album_set.all()
  ```

- Create

  ```sql
  artist = Artist.objects.get(id=1)
  genre = Genre.objects.get(id=1)
  
  album = Album()
  album.name = '앨범1'
  album.artist = artist # 1. 객체의 저장
  album.genre = genre
  album.save()
  ```

