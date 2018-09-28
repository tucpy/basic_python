'''
Tinh S (dien tich)/P(chu vi) hinh tron voi tham so r
Tinh S/P hinh chu nhat voi tham so a,b (chieu dai, chieu rong)
'''

import math
s_tron = lambda r: math.pi * math.pow(r,2)
p_tron = lambda r: r * 2 * math.pi

s_chu_nhat = lambda a, b: a * b
p_chu_nhat = lambda a, b: (a + b) * 2

print(s_tron(4))
print(p_tron(4))

print(s_chu_nhat(2,4))
print(p_chu_nhat(2,4))