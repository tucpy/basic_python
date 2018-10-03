'''
Build-in function map(), reduce(), filter() 
'''

#Tinh tong cac phan tu trong list:

from functools import reduce
from operator import add
day_so = [-4,-9, 2, 3, 7, 13, 20]
sum = reduce(add, day_so)
print("Tong: ", sum)

# List cac so lon hon x:
x = int(input("x: "))

day_so_x = list(filter(lambda item: item > x, day_so))
print("Cac so lon hon x: ", day_so_x)

# List cac so nguyen to:

#so_nguyen_to = list(filter(lambda item: (item for item in day_so if (item % j == 0 for j in range(2, item)) and item > 0), day_so))
#print("So nguyen to: ", so_nguyen_to)

#isprime = lambda x: int(x) > 0 and (x == 2 or x == 3 or [x % i == 0 for i in range(2,int(x**0.5)+1)].count(True) == 0)

# List cac phan tu am:
list_am = list(filter(lambda item: item < 0, day_so))
print("Cac so am", list_am)
# List cac phan tu duong:
list_duong = list(filter(lambda item: item > 0, day_so))
print("Cac so duong", list_duong)