# 문자열 포맷
# 1. format()
a = 'Python'
b = 'C'
c = 'Java'

print("a : {}, b : {}, c : {}".format(a, b, c))
print("c : {2}, b : {1}, a : {0}".format(a, b, c))
print("c : {p1}, b : {p2}, a : {p3}".format(p1=a, p2=b, p3=c))

# 2. f'strings
x = 10
y = 20

print(f"{x} + {y} = {x + y}")

pi = 3.141592
print(f"PI 원주율 : {pi:.2f}")
# :.2f  - 소수점아래 2자까지 표현

from datetime import datetime

today = datetime.now()
print(f"오늘 날짜 : {today:%Y-%m-%d %H:%M:%S}")
