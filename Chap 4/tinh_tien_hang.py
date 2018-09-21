so_luong = int(input('Nhập số lượng: '))
don_gia = int(input('Nhập đơn giá: '))

thanh_tien = so_luong * don_gia

if so_luong >= 5:
    tien_giam = thanh_tien * 0.1
    thanh_tien *= 0.9
    # thanh_tien = thanh_tien * 0.9
    print("Thành tiền = %i * %s - %s = %s" %(so_luong, "{:,}".format(don_gia), "{:,}".format(tien_giam), "{:,}".format(thanh_tien) + " VNĐ"))
else:
    print("Thành tiền = %i * %s = %s" %(so_luong, "{:,}".format(don_gia), "{:,}".format(thanh_tien) + " VNĐ"))
