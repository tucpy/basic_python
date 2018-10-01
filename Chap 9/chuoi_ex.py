'''
Cho chuoi " Trung Tam TiN Hoc"
Dem so ki tu in hoa va in thuong, ko dem khoang trang

dic = { "Hoa": 0
        "Thuong": 0}
Chay trong vong lap, neu gap 1 chu hoa thi cap nhat dic
'''

chuoi = "Trung Tam TiN Hoc"
b = list(chuoi)
print(chuoi)
print(b)

count_hoa = 0
count_thuong = 0

for i in chuoi:
    if i.isupper(): # ban dau dung chuoi.isupper() -> ko ra vi luc nay xet toan bo chuoi, neu hoa het moi la True
        count_hoa += 1
    if i.islower():
        count_thuong += 1

print("So chu hoa: ", count_hoa)
print("So chu thuong: ", count_thuong)

'''
#Thay sua:

string = input("Nhập câu của bạn: ")
dic = {"HOA": 0, "THUONG": 0}

for char in string:
    if char.isupper():
        dic["HOA"] += 1
    elif char.islower():
        dic["THUONG"] += 1

print("Chữ hoa:", dic["HOA"])
print("Chữ thường:", dic["THUONG"])
'''