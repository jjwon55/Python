# 멤버쉽 연산자
# - 어떤 값이 지정한 컬렉션에 포함되어 있는지 여부를 반환하는 연산자
# a in c : 포함 True, 미포함 False
# a not in c : 미포함 True , 포함 False

a = [1,2,3]
b = [4,5,6]

x = 3 in a
y = 10 in a
z = 100 not in b
print('x : {}'.format(x))
print('y : {}'.format(y))
print('z : {}'.format(z))