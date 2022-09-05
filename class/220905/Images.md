### Images

##### Responsive images

```html
<img src="..." class="img-fluid" alt="...">

<!--
bootstrp의 이미지는 img-fluid로 반응
-->
```

##### Image thumbnails

```html
<img src="..." class="img-thumbnail" alt="...">

<!-- img-thumbnail == border-radius -->
```

##### Aligning images

```html
<img src="..." class="rounded float-start" alt="...">
<img src="..." class="rounded float-end" alt="...">

<img src="..." class="rounded mx-auto d-block" alt="...">

<div class="text-center">
  <img src="..." class="rounded" alt="...">
</div>

<!-- 
float클래스로 텍스트나 이미지 정렬
mx-auto를 사용하여 중앙에 배치 가능
```

##### Picture

```html
<picture>
  <source srcset="..." type="image/svg+xml">
  <img src="..." class="img-fluid img-thumbnail" alt="...">
</picture>

<!-- 
picture을 사용하여 img에 source요소를 지정하는 경우 img에 추가해야함
```

