# 리스트는 mutable
a = [1, 2, 3]
a[0] = 100
print(a)
# [100, 2, 3]

# 문자열은 immutable
a = 'hi'
a[0] = 'c'
print(a)
# Traceback (most recent call last):
#  File "C:\Users\dwde2\Desktop\수업연습\0714\04.mutable.py", line 8, in <module>
#    a[0] = 'c'
# TypeError: 'str' object does not support item assignment