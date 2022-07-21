sum = 5
print(sum([1, 2, 3]))

# Traceback (most recent call last):
#  File "C:\Users\dwde2\Desktop\수업연습\0713\05_LEGB.py", line 2, in <module>
#    print(sum([1, 2, 3]))
# TypeError: 'int' object is not callable

# sum이 지금은 5가 되어버림
# Buil-in scope에 sum 함수가 있었음
# Global scope에 sum이름의 변수를 만들었음
# 찾으니까 L -> E -> G -> B