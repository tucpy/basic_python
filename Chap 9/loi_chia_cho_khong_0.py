'''
a = 24
b = int(input("Nhập số chia: "))
print("Kết quả %i chia cho %i là %f:" % (a, b, a/b))
'''

try:
    a = 24
    b = int(input("Nhập số chia: "))
    kq = a/b
    print("Kết quả %i / %i = %f" % (a, b, kq))
except ZeroDivisionError as loi:
    print("Lỗi:", loi)
except ValueError as loi2:
    print("Lỗi 2: ", loi2)