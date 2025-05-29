a = 10
b = 5

result1 = a > 7
result2 = b > 7
result3 = a < 7
result4 = b < 7


print('{} > 7 and {} > 7 : {}'.format(a, b, result1 and result2))   # 1
print('{} > 7 or {} > 7 : {}'.format(a, b, result1 or result2))     # 2 쇼트 서킷


print('{} > 7 and {} < 7 : {}'.format(a, b, result3 and result4))   # 3 쇼트 서킷
print('{} > 7 or {} < 7 : {}'.format(a, b, result3 or result4))     # 4

print('not a : {} : {}'.format(a, not a))
print('not 0 : {} : {}'.format(0, not 0))