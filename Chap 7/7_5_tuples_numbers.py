'''
Tạo tuple a chứa 4 số nguyên dương
tuple b chứa 4 số nguyên dương tiếp theo
tuple c là kết hợp a và b
tuple d là tuple c đã được sắp xếp
in phần tử thứ 3 của tuple d
in 3 phần tử cuối của tuple d

'''

tup_a = (3, 1, 2, 4)
tup_b = (5, 7, 6, 8)
tup_c = tup_a + tup_b
print(tup_c)
tup_d = sorted(tup_c)
print(tup_d)
print(tup_d[2])
print(tup_d[5:8])