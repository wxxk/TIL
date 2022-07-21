from turtle import st


name = '동현'
name1 = '효근'
name2 = '수경'
name3 = '나영'
name4 = '다겸'
name5 = '예지'

# 리스트
# 값들의 나열
students = ['동현', '효근', '수경', '나영', '다겸', '예지']
# 인덱스 순서로 접근
print(students[0])
print(students[-1])

students_1 = ['동현', '효근']
students_2 = ['수경', '나영']
students_3 = ['다겸', '예지']

students = [['동현', '효근'], ['수경', '나영'], ['다겸', '예지']]

# 딕셔너리
# 키-값의 쌍
students = {'1회차': ['동현', '효근'], 
            '2회차': ['수경', '나영'],
            '3회차': ['다겸', '예지']
}
# 접근할 때 키로 접근합니다.
print(students['1회차'])