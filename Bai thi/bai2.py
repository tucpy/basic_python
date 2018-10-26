'''
Tinh thue thu nhap ca nhan
'''

bac1 = 0.05
bac2 = 0.1
bac3 = 0.15
bac4 = 0.2
bac5 = 0.25
bac6 = 0.3
bac7 = 0.35

bac = {"1": 0.05, "2": 0.1, "3": 0.15, "4": 0.2, "5": 0.25, "6": 0.3, "7": 0.35}

thu_nhap = int(input("Thu nhap hang thang: "))
phu_thuoc = int(input("So nguoi phu thuoc: "))
mien = int(input("Cac khoan duoc mien: "))


thu_nhap_chiu_thue = thu_nhap - mien
giam_tru = 9000000 + (phu_thuoc * 3600000)

thu_nhap_tinh_thue = thu_nhap_chiu_thue - giam_tru


if thu_nhap_tinh_thue < 5000000:
    thue = thu_nhap_tinh_thue * bac1
elif thu_nhap_tinh_thue >= 



