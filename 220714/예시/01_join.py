names = ','.join(['홍길동', '김철수'])
print(names)
# 홍길동,김철수

# numbers = ' '.join([10, 20, 100])
numbers = ' '.join(map(str, [10, 20, 100]))
print(numbers)
# Traceback (most recent call last):
#  File "C:\Users\dwde2\Desktop\수업연습\0714\01_join.py", line 5, in <module>
#    numbers = ' '.join([10, 20, 100])
# TypeError: sequence item 0: expected str instance, int found