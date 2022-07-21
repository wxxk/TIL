# 👨🏻‍🤝‍👨🏻Git Flow

> Git을 활용하여 협업하는 흐름으로 branch를 활용하는 전략을 의미



[branch 실습](./branch_practice.md)

[fork 실습](./fork_practice.md)

---



### Branch basic commands

- 브랜치 생성

```bash
(master) $ git branch <브랜치 이름>
```

- 브랜치 이동

```bash
(master) $ git checkout <브랜치 이름>
```

- 브랜치 생성 및 이동

```bash
(master) $ git checkout -b <브랜치이름>
```

- 브랜치 목록

```bash
(master) $ git branch
```

- 브랜치 삭제

```bash
(master) $ git branch -d <브랜치 이름>
```

- 그래프형태

```bash
$ git log --oneline --branch
```



---



### Github Flow Models

> 해당 프로젝트 저장소에 직접적인 push 권한이 있는지의 여부

#### Feature Branch Workflow (저장소의 소유권이 있는 경우)

1. 혼자작업, 조원 프리라이딩(Fast-forward)
2. 서로 다른 이력을 병합하는 과정에서 다른 파일이 수정되어 있는 상황
3. 각자 커밋이 있는데, 같은 파일이 수정



#### Forking Workflow (저장소의 소유권이 없는 경우)

1. 소유권이 없는 원격 저장소를 fork를 통해 복제
2. 추후 로컬 저장소를 원본 원격 저장소와 동기화하기 위해 URL을 연결
3. 기능 추가를 위해 branch 생성 및 기능 구현
4. 기능 구현 후 원격 저장소에 브랜치 반영
5. Pull requests 요청
6. 병합 완료/ 완료 된 브랜치 삭제
7. master 브랜치로 switch
8. 병합된 master의 내용을 pull
9. 원격 저장소에서 병합 완료 된 로컬 브랜치 삭제
10. 새로운 기능 추가를 위해 branch 생성 및 과정 반복

---



### branch 예시

0. branch 전 작업

> root commit을 발생시키는 작업(master)

```bash
$ git add 

$ git commit -m '<>'
```



1. branch 

> 브랜치에서 작업을 한 이후 이력을 합치기 위해서 일반적으로 merge 를 사용

```bash
$ git init #저장소 설정

$ touch README.md #첫번째 커밋

$ git add README.md

$ git commit -m 'Add README' #(root-commit)

$ git branch #브랜치 조회

git $ git branch example #example 이라는 이름의 브랜치 생성

$ git checkout example #브랜치 이동 (master -> example)
```

- 브랜치할때 가장 중요한것은 첫번재 커밋
- (master) 는 브랜치를 의미



2. 작업 후 (브랜치 : example)

```bash
$ git status

$ git add .

$ git commit -m '예시 만듬'

$ git log --oneline #작업한 로그 확인

$ git checkout master #master 브랜치로 돌아감

$ git log --oneline #example.txt 사라짐
```

- HEAD의 의미 : 전체 중에 내가이동한 정보의 위치를 가지고있다



3. 합치기

```bash
(master)$ git merge example #병합

$ git log --oneline

$ git branch

$ git branch -d example #example브랜치를 지운다

$ git log --oneline
```

- 브랜치/git/github -> 작업/협업을 위한 것

- 붙이는 메인이 되는 브랜치에 병합