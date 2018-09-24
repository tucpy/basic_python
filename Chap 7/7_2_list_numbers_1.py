
tiep_tuc = True
day_so =[]
while (tiep_tuc):
    so = int(input("Nhap gia tri: "))
    day_so.append(so)
    nhap = int(input("Tiep tuc nhap gia tri? 1: Co, 0: Khong\n"))
    if nhap == 1:
        tiep_tuc = True
    else:
        tiep_tuc = False

x = int(input("Nhap gia tri can tim x:"))
print(day_so)

# Tinh tong cac gia tri trong list
tong = 0
for i in day_so:
    tong += i
print("Tong cac gia tri trong list: %d" %tong)

# Xet xem x co xuat hien trong list? Neu co thi bao nhieu lan?
count = 0
for i in day_so:
    if x == i:
        count += 1
        #print (i)
    else:
        count += 0

if count != 0:
    print ("%i xuat hien %i lan trong danh sach" %(x,count))
else:
    print("%i khong co trong danh sach" %x)

# Xet xem x co lon hon cac so con lai khong?
lon_hon_x = []
count_new = 0
for i in day_so:
    if x < i:
        lon_hon_x.append(i)
        count_new += 0

# In cac so lon hon x:
if count_new == 0:
    print("%i khong lon hon tat ca cac so trong list" %x)
    print("Cac so lon hon",x,"trong list: ",lon_hon_x)
else:
    print("%i lon hon %i so trong list" %(x,count))
    print("Cac so lon hon",x,"trong list: ",lon_hon_x)


