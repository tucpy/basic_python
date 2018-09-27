day_so = []
tiep_tuc = True

# Nhap day so mong muon
while tiep_tuc:
    n = int(input("Nhap gia tri: "))
    day_so.append (n)
    tiep_tuc = int(input("Tiep tuc nhap gia tri? 1: Co. 0: Khong "))
    if tiep_tuc == 1:
        tiep_tuc = True
    else:
        tiep_tuc = False

# Tim va in ra cac so nguyen to co trong list -> fix tai sao so am van la so nguyen to
so_nguyen_to =[]
so_nguyen_to =[i for i in day_so if (all(i % j != 0 for j in range(2, i)))]

print("So nguyen to: ", so_nguyen_to)


# Tinh trung binh cong cua cac phan tu am/ phan tu duong trong list
sum_am = 0
sum_duong = 0
count = 0
# Tinh tong
for i in day_so:
    if i < 0:
        sum_am += i
        count +=1
    else:
        sum_duong += i
        count +=1

# List cac phan tu am va duong
day_am = []
day_duong = []
for i in day_so:
    if i < 0:
        day_am.append(i)
    else:
        day_duong.append(i)
print("Cac phan tu am trong list: ", day_am)
# Count so phan tu -> tinh trung binh
print("Trung binh cong so am: ", sum_am/count)

print("Cac phan tu duong trong list: ", day_duong)
print("Trung binh cong so duong: ", sum_duong/count)


# Tim gia tri lon nhat/ nho nhat trong list
print("So lon nhat: ", max(day_so))

print("So nho nhat: ", min(day_so))

#Sap xep list theo thu tu tang dan
day_so.sort()
print("List sap xep tang dan: ", day_so)