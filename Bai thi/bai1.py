'''
Nhap chuoi 
'''

tiep_tuc = True

ds = []
while tiep_tuc == True:
    chuoi = str(input("Nhập chuỗi (dừng lại => bấm phím s) :"))
    if chuoi == "s":
        tiep_tuc = False
    else:
        ds.append(chuoi)
        tiep_tuc = True

# Viet hoa chuoi, in chieu dai chuoi
for i in ds:
    length = len(i)
    print(i.upper(), "(%i)" %length)

# In ra man hinh chuoi dai nhat
print ("Chuoi dai nhat la'",max(ds),"' tai vi tri", ds.index(max(ds)))




