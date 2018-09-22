import time

'''
print(time.time())
'''

'''
print(time.localtime(time.time()))
'''

'''
print(time.asctime(time.localtime(time.time())))
'''

'''
from datetime import datetime
print(datetime.now())

print(datetime(2018,8,7))
'''


import calendar

'''
print(calendar.monthcalendar(2018,9))

print(calendar.weekday(2018,9,21))

print(calendar.monthrange(2018,9))
'''

'''
calendar1 = calendar.monthrange(2018,9)
print(calendar1[1])
'''



nam = int(input("Nhập năm: "))
thang = int(input("Nhập tháng: "))


# Cách 1
'''
if (thang in [1,3,5,7,8,10,12]):
    print("Tháng %i năm %i có 31 ngày" %(thang, nam))
elif (thang in [4,6,9,11]):
    print("Tháng %i năm %i có 30 ngày" %(thang, nam))
else:
    if calendar.isleap(nam) == True:
        print("Tháng %i năm %i có 29 ngày" %(thang, nam))
    else:
        print("Tháng %i năm %i có 28 ngày" %(thang, nam))
'''

# Cách 2
so_ngay = calendar.monthrange(nam, thang)
print("Tháng %i năm %i có %i ngày" %(thang, nam, so_ngay[1]))

