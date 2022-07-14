# 문자의 위치 구하기

word = input()

# 1. for - else
# 문자로 순회하는 것이 아니라 인덱스로 접근!!
# 원하는 숫자 0 1 2 3 4 5
# 얻는 방법 range(len(word))
for idx in range(len(word)):
    # print(word[idx])
    # 알파벳이 a일때
    if word[idx] == 'a':
        print(idx)
        break
# for문을 다 돌았다는 뜻은
# 한번도 break에 안 걸렷다
# 즉, a는 없었다.
else:
    print(-1)


# 2. for - else 안쓸 때
# a가 있었냐? 없었냐? (boolean)
is_a = False
for idx in range(len(word)):
        if word[idx] == 'a':
            print(idx)
            is_a = True
            break

if is_a == False:
    print(-1)