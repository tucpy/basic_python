loai_xe = int(input("Loại xe nào (4 ==> 4 chổ ; 7 ==> 7 chổ): "))
so_km = int(input("Số km: "))
thoi_gian_cho = int(input("Thời gian chờ: "))

if loai_xe == 4:
    # Tính toán
    # Tính tiền chờ
    if thoi_gian_cho > 5:
        tien_cho = (thoi_gian_cho - 5) * 750
    else:
        tien_cho = 0
    print("Tiền chờ:", tien_cho)

    # Tính tiền di chuyên
    if so_km <= 0.8:
        tien_di_chuyen = 11000
    elif so_km < 31:
        tien_di_chuyen = 11000 + (so_km - 0.8) * 15300
    else:
        tien_di_chuyen = 11000 + (31 - 0.8) * 15300 + (so_km - 31) * 12100
    print("Tiền di chuyển:", tien_di_chuyen)
    
    # Tính tiền cước
    tien_cuoc = tien_di_chuyen + tien_cho

    # Xuất
    print("Tiền cước:", tien_cuoc)

elif loai_xe == 7:
    pass
else:
    print("Không có xe!")