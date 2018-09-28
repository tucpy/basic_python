# lambda a: a*2 => là hàm lambda
# a là tham số
# a*2 là biểu thức
'''
nhan_doi = lambda a: a*2
print(nhan_doi(10))

def nhan_doi_2(a):
    return a*2
print(nhan_doi_2(10))
'''

# Tính điểm trung bình
'''
diem_tb = lambda hk1, hk2: (hk1+hk2*2)/3
print(diem_tb(7, 8))
'''




# Tính s = (x*x+1)^n
import math
s = lambda x,n: math.pow(math.pow(x,2)+1,n)
kq = s(4,6)
print(kq)

def s1(x,n):
    kq = math.pow(math.pow(x,2)+1,n)
    return kq
kq1 = s1(4,6)
print(kq1)


# map()
'''
list_one = [1,2,3]
list_three = [6,7,8,9,10]
print("list_one:", list_one)

list_two = list(map(lambda item: item**2, list_one))
print("list_two:", list_two)

four = lambda item1, item2: item1 + item2

list_four = list(map(four, list_one, list_three))
print("list_four:", list_four)
'''

'''
list_new = list(map(lambda item1, item2: item1 + item2, [1,2,3,4], [2,3,4,5]))
print("list_new:", list_new)
'''


# https://docs.python.org/2/library/operator.html
from operator import add
list_add = list(map(add, {6:"abc",4:"def"}, [3,2]))
print("list_add:", list_add)



'''
a = list("hello ababababa")
print(a)
'''

# filter()
'''
list_string = ["abc", "def", "abf", "stu", "cba"]
list_string_a = list(list_string)
print(list_string_a)

list_string_b = list("hello ababababa")
print(list_string_b)
'''

# reduce()
'''
tong = 0
list_number = [1,2,3,4,5,6,7,8,9,10]
for num in list_number:
    tong = tong + num
print(tong)
'''

'''
from functools import reduce
list_number = [1,2,3,4,5,6,7,8,9,10]
sum1 = reduce(lambda item1, item2: item1 + item2, list_number)
print(sum1)
'''