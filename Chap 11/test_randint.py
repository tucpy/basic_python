from random import randint

Danh_sach_ban_be = {"01235468655": "Nguyễn Văn A", 
                    "0909090909": "Trần Thị B",
                    "0936514588": "Hồ Ngọc C"}

cac_key = list(Danh_sach_ban_be.keys())
print(cac_key)

i = randint(0, len(Danh_sach_ban_be) - 1)
lay_key = cac_key[i]
print(lay_key)

lay_value = Danh_sach_ban_be[lay_key]
print(lay_value)
