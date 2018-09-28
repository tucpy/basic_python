'''
Bai 5_1: tinh_S(n,x). S = (x^2 + 1)^n
'''

import math
def tinh_S(n,x):
    S = pow((pow(x,2) + 1), n)
    return S

'''
Bai 5_2: tinh_A(n,x). A = (x^2 + x + 1)^n + (x^2 - x + 1)^n
'''

import math
def tinh_A(n,x):
    A = pow((pow(x,2) + x + 1), n) + pow((pow(x,2) - x + 1), n)
    return A

'''
Bai 5_3: kiem_tra_so_nguyen_to(x)
'''

nt = True
def kiem_tra_so_nguyen_to(x):
    for i in range(2,x):
        if x % i != 0:
            nt = True
            return nt
        else:
            nt = False
            return nt


print(kiem_tra_so_nguyen_to(-4))
print(kiem_tra_so_nguyen_to(10))

'''
# tinh tong S = x + y
S = lambda x,y : x + y
print(S(4,8))

'''
