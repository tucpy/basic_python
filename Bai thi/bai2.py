'''
Tinh thue thu nhap ca nhan
'''
bac = {"1": 0.05, "2": 0.1, "3": 0.15, "4": 0.2, "5": 0.25, "6": 0.3, "7": 0.35}


thu_nhap = int(input("Thu nhap hang thang: "))
phu_thuoc = int(input("So nguoi phu thuoc: "))
mien = int(input("Cac khoan duoc mien: "))

thu_nhap_chiu_thue = thu_nhap - mien
giam_tru = 9000000 + (phu_thuoc * 3600000)

thu_nhap_tinh_thue_ori = thu_nhap_chiu_thue - giam_tru
thu_nhap_tinh_thue = thu_nhap_tinh_thue_ori

# Cach 1: dung vong lap while
tien_thue = 0
tong_thue = 0
while (thu_nhap_tinh_thue > 0):
    if thu_nhap_tinh_thue > 80000000:
        tien_thue = (thu_nhap_tinh_thue - 80000000) * 0.35
        thu_nhap_tinh_thue -= 80000000
        tong_thue += tien_thue
    elif thu_nhap_tinh_thue > 52000000:
        tien_thue = (thu_nhap_tinh_thue - 52000000) * 0.3
        thu_nhap_tinh_thue -= 52000000
        tong_thue += tien_thue
    elif thu_nhap_tinh_thue > 32000000:
        tien_thue = (thu_nhap_tinh_thue - 32000000)* 0.25
        thu_nhap_tinh_thue -= 32000000
        tong_thue += tien_thue
    elif thu_nhap_tinh_thue > 18000000:
        tien_thue = (thu_nhap_tinh_thue - 18000000) * 0.2
        thu_nhap_tinh_thue -= 18000000
        tong_thue += tien_thue
    elif thu_nhap_tinh_thue > 10000000:
        tien_thue = (thu_nhap_tinh_thue - 10000000) * 0.15
        thu_nhap_tinh_thue -= (thu_nhap_tinh_thue - 10000000)
        tong_thue += tien_thue
    elif thu_nhap_tinh_thue > 5000000:
        tien_thue = (thu_nhap_tinh_thue - 5000000) * 0.1
        thu_nhap_tinh_thue -= (thu_nhap_tinh_thue - 5000000)
        tong_thue += tien_thue
    else:
        tien_thue = thu_nhap_tinh_thue * 0.05
        tong_thue += tien_thue
        thu_nhap_tinh_thue = 0

print("Thu nhap tinh thue / thang:" "{:,}".format(thu_nhap_tinh_thue_ori)) 
print("Tien thue phai nop / thang:" "{:,}".format(tong_thue))

# Cach 2: dung list