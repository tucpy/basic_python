'''
Danh_sach_ban_be = {"01235468655": "Nguyễn Văn A", "0909090909": "Trần Thị B"}
Xuat danh sach ban be: 
So dien thoai           Ho ten
--------------------------------
01235468655             Nguyễn Văn A
0909090909              Trần Thị B

'''

ds_ban_be = {"01235468655": "Nguyễn Văn A", "0909090909": "Trần Thị B"}

#print(ds_ban_be)

#print(ds_ban_be["01235468655"])
#print(ds_ban_be["0909090909"])

print ("\nSo dien thoai".ljust(20), "Ho ten".ljust(50))
print("-" * 40)

for i in ds_ban_be:
    print(i.ljust(20), ds_ban_be[i].ljust(50))

'''
Them moi so dien thoai, neu sdt (key) co ton tai, ko duoc cap nhat

1. In danh sach
2. Them moi
3. Cap nhat danh sach
In danh sach cap nhat
'''



'''
Thay sua:
Danh_sach_ban_be = {"01235468655": "Nguyễn Văn A", "0909090909": "Trần Thị B"}
# print(Danh_sach_ban_be)
# Xuất danh sách
print("\nSĐT".ljust(20) + "HỌ TÊN".ljust(50))
print("- "*25)
for sdt in Danh_sach_ban_be:
    print(sdt.ljust(20) + Danh_sach_ban_be[sdt].ljust(50))
    print(sdt.ljust(20) + Danh_sach_ban_be.get(sdt).ljust(50))

'''