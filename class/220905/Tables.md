### Tables

---

##### overview

```html
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td colspan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
```

##### Variants

```html
<!-- On tables -->
<table class="table-primary">...</table>
<table class="table-secondary">...</table>
<table class="table-success">...</table>
<table class="table-danger">...</table>
<table class="table-warning">...</table>
<table class="table-info">...</table>
<table class="table-light">...</table>
<table class="table-dark">...</table>

<!-- On rows -->
<tr class="table-primary">...</tr>
<tr class="table-secondary">...</tr>
<tr class="table-success">...</tr>
<tr class="table-danger">...</tr>
<tr class="table-warning">...</tr>
<tr class="table-info">...</tr>
<tr class="table-light">...</tr>
<tr class="table-dark">...</tr>

<!-- On cells (`td` or `th`) -->
<tr>
  <td class="table-primary">...</td>
  <td class="table-secondary">...</td>
  <td class="table-success">...</td>
  <td class="table-danger">...</td>
  <td class="table-warning">...</td>
  <td class="table-info">...</td>
  <td class="table-light">...</td>
  <td class="table-dark">...</td>
</tr>
```



### Accented tables

##### Striped rows

```html
<table class="table table-striped">
  ...
</table>

<table class="table table-dark table-striped">
  ...
</table>

<table class="table table-success table-striped">
  ...
</table>

<!-- table table-stripe : 얼룩말 줄무늬 추가 -->
```

##### Striped columns

```html
table class="table table-striped-columns"

<!-- table table-striped-columns : 열에 무늬 추가 -->
```

##### Hoverable rows

```html
class="table table-hover"
```

##### Active tables

```html
class="table-active"

<!-- 테이블 행이나 셀을 강조 -->
```



### Table borders

##### Bordered tables

```html
class="table table-bordered"

<!-- 테두리 표시-->

class="table table-bordered border-primary"
<!-- 파란색 테두리 표시-->

class="table table-borderless
<!-- 테이블 테두리 없음-->
```

##### Small tables

```html
class="table table-sm"

<!-- 모든 셀 padding을 반으로 잘라 .table을 더 간결하게 만듭니다. -->
```

##### Table group dividers

```html
class="table-group-divider"

<!-- tbody, tfoot 사이에 두꺼운 테두리 추가 -->
```

##### Vertical alignment

```html
class="table-responsive"
class="table align-middle"
class="align-bottom"
class="align-top"

<!--
table-responsive : 수직정렬 
table align-middle : 중간
align-bottom : 밑
align-top : 위
-->
```

##### Nesting

```html
class="table table-striped"

<!--
Nesting(중첩) - 테두리 스타일, 활성 스타일 및 테이블 변형은 중첩 테이블에서 상속되지 않음.
-->
```



### Anatomy

##### Table head

```html
<table class="table">
  <thead class="table-light">
      
<table class="table">
  <thead class="table-dark">
      
<!-- 
테이블 헤드 
-->
```

##### Captions

```html
<table class="table table-sm">
  <caption>List of users</caption>
    
<table class="table caption-top">
  <caption>List of users</caption>

<!--
Captions - 표의 제목과 같은 기능
-->
```



### Responsive tables

##### Always responsive

```html
<div class="table-responsive">
  <table class="table">
      
<!-- 항상 반응형 : 수평 스크롤에 .table-responsive 사용 -->      
```

##### Breakpoint specific

```html
<div class="table-responsive">
  <table class="table">
      
<div class="table-responsive-sm">
  <table class="table">
      
<div class="table-responsive-md">
  <table class="table">
      
<div class="table-responsive-lg">
  <table class="table">     
      
<div class="table-responsive-xl">
  <table class="table">
      
<div class="table-responsive-xxl">
  <table class="table">
      
<!--
중단점으로 구분 : 특정 중단점까지 반응형 테이블을 생성 
.table-responsive{-sm|-md|-lg|-xl|-xxl}
-->
```

