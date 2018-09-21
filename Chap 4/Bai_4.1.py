# 4.1: Max / Min
a, b, c, d = eval(input('Nhập a, b, c, d: '))
print('a, b, c, d = ', a, b, c, d)

soMax = a
if soMax < b:
    soMax = b
if soMax < c:
    soMax = c
if soMax < d:
    soMax = d
print('Max =', soMax)

soMin = a
if soMin > b:
    soMin = b
if soMin > c:
    soMin = c
if soMin > d:
    soMin = d
print('Min =', soMin)
