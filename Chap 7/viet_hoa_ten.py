
chuoi = str(input("Nhap ho va ten: "))

list_tu = chuoi.split()
print(list_tu)

chuoi_xu_ly =""
for tu in list_tu:
    tu_xu_ly = tu.capitalize()
    chuoi_xu_ly += tu_xu_ly +" "
print(chuoi_xu_ly)