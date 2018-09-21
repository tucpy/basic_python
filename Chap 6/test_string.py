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