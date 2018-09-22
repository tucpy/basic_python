
n = int(input("Ban muon nhap bao nhieu so: "))


danh_sach = []
for i in range(0,n):
    so = int(input("Nhap so thu %i: " %(i+1)))
    danh_sach.append(so)

print(danh_sach)

tong = 0
for j in danh_sach:
    tong += i

trung_binh = tong / n
print ("Tong:", tong)
print ("Trung binh: ", trung_binh)
