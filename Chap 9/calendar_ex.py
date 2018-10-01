'''
Nhap vao thang va nam -> xuat ra so ngay trong thang
Ngay cuoi cua thang la thu may?

'''

from datetime import datetime
import calendar

thang = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))

thang_31 = [1,3,5,7, 8, 10, 12]
thang_30 = [4,6,9,11]


#Xuat ra so ngay trong thang
if thang == 2 and calendar.isleap(nam) == True:
    ngay = 28
    print("Thang 2 nam",nam,"co 29 ngay")
elif thang == 2 and calendar.isleap(nam) == False:
    ngay = 29
    print("Thang 2",nam, "co 28 ngay")
else:
    for item in thang_31:
        if thang == item:
            ngay = 31
            print("Thang %i nam %i co 31 ngay" %(thang, nam))
    for item in thang_30:
        if thang == item:
            ngay = 30
            print("Thang %i nam %i co 30 ngay" %(thang, nam))


# Ngay cuoi cung cua thang, nam do la thu may?
#calendar.weekday(nam, thang, ngay)

#print(calendar.weekday(nam, thang, ngay))

thu = {0: "thu hai", 1:"thu ba", 2: "thu tu", 3: "thu nam", 4: "thu sau", 5: "thu bay", 6: "chu nhat"}

print("Ngay cuoi cung trong thang la", thu[calendar.weekday(nam, thang, ngay)])


'''
Thay sua:

import calendar
thang = int(input("\nNhập tháng: "))
nam = int(input("Nhập năm: "))

so_ngay_trong_thang = calendar.monthrange(nam, thang)
print("Tháng %i năm %i có %i ngày" %(thang, nam, so_ngay_trong_thang[1]))
thu_ngay_cuoi = calendar.weekday(nam, thang, so_ngay_trong_thang[1])

list_thu = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]
print("Ngày cuối cùng của tháng %i năm %i là ngày %s" %(thang, nam, list_thu[thu_ngay_cuoi]))


'''


