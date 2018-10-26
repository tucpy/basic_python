'''
Nhap thang, nam
Xuat thang do nam do co bao nhieu ngay?
'''

import calendar

thang = int(input("Thang: "))
nam = int(input("Nam: "))

# Cach 1:
if thang > 0 and nam > 0:

    if thang in [1,3,5,7,8,10,12]:
        print(thang, "-", nam, "co 31 ngay")
    elif thang in [4,6,9,11]:
        print("%d thang - %d nam co 30 ngay" %(thang, nam))     
    else:
        if calendar.isleap(nam) == True:
            print("%d thang - %d nam co 29 ngay" %(thang, nam))
        else:
            print("%d thang - %d nam co 28 ngay" %(thang, nam))

else:
    print ("Ngay thang khong hop le")

# Cach 2:
so_ngay = calendar.monthrange(nam, thang)
print("Thang %i nam %i co %i ngay" %(thang,nam,so_ngay[1]))
