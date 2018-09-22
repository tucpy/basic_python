'''
str1 = "123"
str2 = int(str1)
print(type(str2))
'''

'''
so = input("Nhập số: ")

if so.isdigit() == True:
    print("Là số")
else:
    print("Không phải số")
'''

'''
ho_ten = "Nguyễn Thị Bé Ba"
cac_tu = ho_ten.split()
print(cac_tu)

# Họ
ho = cac_tu[0]
print("Họ:", ho)

# Tên
chieu_dai = len(cac_tu)
ten = cac_tu[chieu_dai - 1]
print("Tên: %s" %ten)

# Tên lót
ten_lot = ""
for i in range(1, chieu_dai - 1):
    ten_lot += cac_tu[i] + " "
print("Tên lót:", ten_lot)
'''



chuoi = "trung tâm tin học"
print(chuoi.ljust(30, "*"))
print(chuoi.rjust(30, "*"))
print(chuoi.upper())



print("HỌ".ljust(30, " ") + "TÊN".ljust(10, " ") + "LƯƠNG".rjust(15, " "))
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")


ho = "Vũ Thanh Trúc"
ten = "Bạch"
luong = 1200
print(ho.ljust(30, " ") + ten.ljust(10, " ") + "{:,}".format(luong).rjust(15, " "))

ho = "Nguyễn Kiều Thanh"
ten = "Lịch"
luong = 500
print(ho.ljust(30, " ") + ten.ljust(10, " ") + "{:,}".format(luong).rjust(15, " "))