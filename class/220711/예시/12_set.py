set_a = {1, 2, 3, 1, 1}
set_b = {'hi',1, 2}

# 내부적으로 '표현'만 똑같이 하는 방법
# 순서가 없어요!!

print(set_a) # {1, 2, 3}
print(set_b) # {1, 2, 'hi'}


# 활용 예시
locations = ['서울', '서울', '대구', '제주', '부산', '부산', '대구', '광주', '인천']
print(set(locations))
print(len(set(locations))) # 6
