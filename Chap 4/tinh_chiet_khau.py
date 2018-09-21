soluong = int(input("Nhap so luong: "))
dongia = int(input("Nhap don gia: "))
if soluong >= 5:
    thanhtien = (soluong * dongia)*0.9
    print ("Thanh tien = (%i * %s) * %s = %s" %(soluong, "{:,}".format(dongia), 0.9, "{:,}".format(thanhtien)))
else:
    thanhtien = soluong * dongia
    print ("Thanh tien = %i * %s = %s" %(soluong, "{:,}".format(dongia), "{:,}".format(thanhtien)))
#chi co the dinh dang dau phay luc print, khong phai luc nhap ban dau
