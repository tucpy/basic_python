soluong = int(input("Nhap so luong: "))
dongia = int(input("Nhap don gia: "))
thanhtien = soluong * dongia

#chi co the dinh dang dau phay luc print, khong phai luc nhap ban dau
print ("Thanh tien = %i * %s = %s" %(soluong, "{:,}".format(dongia), "{:,}".format(thanhtien)))