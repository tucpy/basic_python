'''
Tinh cuoc taxi 4 cho, 7 cho

'''

loai_xe = int(input("Nhap loai xe: "))
so_km = int(input("So km di chuyen: "))
thoi_gian_cho = int(input("Thoi gian cho: "))

if so_km<=30 & loai_xe==4:
    tien_di_chuyen = (0.8*11000) + (so_km - 0.8) * 15300
elif so_km >30 & loai_xe ==4:
    tien_di_chuyen = (0.8*11000) + ((30-0.8)*15300) + (so_km-30)*12100
elif so_km<=30 & loai_xe==7:
    tien_di_chuyen = (0.8 *12000) + (so_km - 0.8) * 16100
else so_km>30 & loai_xe==7:
    tien_di_chuyen = (0.8 *12000) + ((30-0.8)*16100) + (so_km-30)*13800

if thoi_gian_cho > 5:
    tien_cho = (thoi_gian_cho - 5) * 750
else:
    tien_cho = 0

tien_cuoc = tien_cho + tien_di_chuyen

print ("Tien di chuyen: ", tien_di_chuyen)
print ("Tien cho: ", tien_cho)
print ("Tien cuoc: ", tien_cuoc)


