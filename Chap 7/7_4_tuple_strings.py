'''

Tao 1 tuple co 10 phan tu chuoi bat ky
Nhap index duong va index am
Nhap chuoi can tim s_find
-> chuong trinh se in tuple
In gia tri cua phan tu trong tuple co index duong va index am
Tim va dem so lan xuat hien cua s_find trong tuple

'''

tuple_color = ('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange', 'red', 'blue')

in_duong = int(input("Nhap so tu 0 den 9: "))
print(tuple_color[in_duong])

in_am = int(input("Nhap so tu -1 den -9: "))
print(tuple_color[in_am])

s_find = str(input("Nhap chuoi can tim: "))
tuple_color.count(s_find)
print(s_find, "xuat hien trong tuple",tuple_color.count(s_find),"lan")