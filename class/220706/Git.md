## ๐ฅ๊ธฐ๋ณธ ๋ช๋ น์ด

`log` : ํ์ฌ ์ ์ฅ์์ ๊ธฐ๋ก๋ ์ปค๋ฐ์ ์กฐํ

```bash 
$ git log

$ git log -1

$ git log -- oneline

$ git log -2 --oneline
```



## ๐ป๊ธฐ์ด ๋ช๋ น์ด

```bash
$ git status : Git ์ ์ฅ์์ ์๋ ํ์ผ์ ์ํ๋ฅผ ํ์ธํ๊ธฐ ์ํ์ฌ ํ์ฉ

$ git init : ๋ก์ปฌ ์ ์ฅ์ ์์ฑ

$ git add <ํ์ผ๋ช> : ํน์  ํ์ผ/ํด๋์ ๋ณ๊ฒฝ์ฌํญ ์ถ๊ฐ
# $ git add . = ์ ์ฒด ํ์ผ

$ git commit -m ''<์ปค๋ฐ๋ฉ์ธ์ง>'' : ์ปค๋ฐ(๋ฒ์  ๊ธฐ๋ก)

$ git status : ์ํ ํ์ธ

$ git log : ๋ฒ์  ํ์ธ
```



## โ์ค์  ํ์ผ

```bash
$ git config --global user.name "username" (GIthub์์ ์ค์ ํ username)

$ git config --global user.email "my@email" (GIthub์์ ์ค์ ํ email)

# ์ค์  ํ์ธ 
$ git config -i

$ git config --global -1

$ git config user.name
```



