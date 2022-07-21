#### 상황1. 혼자작업, 조원 프리라이딩 (fast-forward)

1. develop 이름을 가진 branch 생성 및 이동

```bash
(master)$ git checkout -b develop
Switched to a new branch 'develop'

(develop)$ git branch #브랜치 목록 확인
* develop
  master
  
(develop)$ git status #수정된 파일 확인
On branch develop
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   1.txt
no changes added to commit (use "git add" and/or "git commit -a")

(develop)$ git add . #작업 완료한 파일 추가

(develop)$ git commit -m '1번 상황' #작업 완료 파일 커밋
[develop 4277933] 1번 상황
 1 file changed, 1 insertion(+)
```

2. 병합

```bash
(develop)$ git log --oneline # 로그 확인
4277933 (HEAD -> develop) 1번 상황
4d20d50 (origin/master, master) exe
d68858d png
14691a0 txt

(develop)$ git checkout master #master 브랜치로 이동
Switched to branch 'master'

(master)$ git log --oneline
4d20d50 (HEAD -> master, origin/master) exe
d68858d png
14691a0 txt
```



#### 상황2. 서로 다른 이력을 병합하는 과정에서 다른 파일이 수정되어 있는 상황

> 각각 커밋이 발생 했는데, 다른 파일만 수정된 경우

1. release 이름의 branch 생성 및 이동

```bash
(master)$ git checkout -b release
Switched to a new branch ''
```

2. 작업 완료 후 master branch로 이동

```bash
(release)$ touch 2_1.txt

(release)$ git add .

(release)$ git commit -m 'release 작업'
[release 626f6c4] release 작업
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 2_1.txt
 
(release)$ git checkout master
Switched to branch 'master'
```

3. master branch에서 작업 

```bash
(master)$ touch 2_2.txt

(master)$ git add .

(master)$ git commit -m 'relase 작업2'
[master 758e854] relase 작업2
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 2_2.txt
```

4. 병합

```bash
(master)$ git merge release
Merge made by the 'ort' strategy.
 2_1.txt | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 2_1.txt
```

5. 확인

```bash
(master)$ git log --oneline
758e854 (HEAD -> master) relase 작업2
1ada1b5 (develop) develop 완료
bbdbd64 초기 작업

(master)$ git log --oneline --graph
*   d2da131 (HEAD -> master) Merge branch 'release'
|\
| * 626f6c4 (release) release 작업
* | 758e854 relase 작업2
|/
* 1ada1b5 (develop) develop 완료
* bbdbd64 초기 작업
```



#### 상황3. 각자 커밋이 있는데, 같은 파일이 수정

> 둘다 README.md 수정

1. feature 이름의 branch 생성

```bash
(master)$ git checkout -b feature #branch 생성
Switched to a new branch 'feature'
```

2. feature 작업

```bash
README.md 내용수정 #충돌.

(feature)$ touch 3.txt

(feature)$ git add .

(feature)$ git commit -m 'feature 작업'
[feature bae436c] feature 작업
 2 files changed, 1 insertion(+)
 create mode 100644 3.txt
```

3. master 이동 후 작업

```bash
(feature)$ git checkout master
Switched to branch 'master'

README.md 내용수정 #충돌

(master)$ git add .

(master)$ git commit -m 'ㅡmaster 작업'
[master 347e866] ㅡmaster 작업
 1 file changed, 1 insertion(+)
```

4. 병합

```bash
(master)$ git merge feature #병합
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.

충돌한 README.md 내용 결정

(master|MERGING)$ git add .

(master|MERGING)$ git commit #commit 자동설정
[master 482e4fe] Merge branch 'feature'

(master)$ git log --oneline --graph #내용 확인
*   482e4fe (HEAD -> master) Merge branch 'feature'
|\
| * bae436c (feature) feature 작업
* | 347e866 ㅡmaster 작업
|/
* 05a47a4 초기작업
```

