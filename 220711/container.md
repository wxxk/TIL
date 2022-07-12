### 컨테이너

> 여러 개의 값을 담을 수 있는 것(객체) 으로, 서로 다른 자료형을 저장할 수 있음
>
> ex) List, tuple

- 컨테이너의 분류
  - 순서가 있는 데이터(Ordered) vs 순서가 없는 데이터(Unordered)
  - 순서가 있다 != 정렬되어 있다.
- 시퀀스
  - 문자열 : 문자들의 나열
  - 리스트 : 변경 가능한 값들의 나열
  - 튜플 : 변경 불가능한 값들의 나열
  - 레인지 : 숫자의 나열



- 컬렉션/비스퀀스
  - 세트 : 유일한 값들의 모음
  - 딕셔너리 : 키-값들의 모음



- 시퀀스형 주요 공통 연산자

| 연산             | 결과                                                      |
| ---------------- | --------------------------------------------------------- |
| s[i]             | s 의 i 번째 항목, 0에서 시작합니다.                       |
| s[i:j]           | s 의 i 번째 항목                                          |
| s[i:j:k]         | s 의 i 에서 j 까지 스텝 k 의 슬라이스                     |
| s + t            | s 와  t의 이어 붙이기                                     |
| s * n 또는 n * s | s 를 그 자신에 n 번 더하는 것                             |
| x in s           | s 의 항목 중 하나가 x 와 같으면 True, 그렇지 않으면 False |
| x not in s       | s 의 항목중 하나가 x와 같으면 False, 그렇지 않으면 True   |
| len(s)           | s 의 길이                                                 |
| min(s)           | s 의 가장 작은 항목                                       |
| max(s)           | s 의 가장 큰항목                                          |