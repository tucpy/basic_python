# try ... except

try:
    a = 24
    b = int(input("Nhập số chia: "))
    kq = a/b
    #print("Kết quả %i / %i = %f" % (a, b, kq))
except ZeroDivisionError as loi1:
    print("Lỗi 1:", loi1)
except ValueError as loi2:
    print("Lỗi 2", loi2)
else:
    print("Kết quả %i + %i = %f" % (a, b, a+b))
    print("Kết quả %i - %i = %f" % (a, b, a-b))
    print("Kết quả %i x %i = %f" % (a, b, a*b))
    print("Kết quả %i / %i = %f" % (a, b, kq))



# Gộp nhiều lỗi vào chung 1 exception
'''
try:
    a = 24
    b = int(input("Nhập số chia: "))
    kq = a/b
    #print("Kết quả %i / %i = %f" % (a, b, a/b))
except (ZeroDivisionError, ValueError) as loi:
    print("Lỗi:", loi)
else:
    print("Kết quả %i + %i = %f" % (a, b, a+b))
    print("Kết quả %i / %i = %f" % (a, b, kq))
'''