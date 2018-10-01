# Cách 1
try:
    a = 24
    b = int(input("Nhập số chia: "))
    if b == 0:
        raise ZeroDivisionError("b phải khác 0")
    kq = a/b
except ZeroDivisionError as loi:
    print("Lỗi:", loi)
else:
    print("Kết quả %i + %i = %f" % (a, b, a+b))
    print("Kết quả %i - %i = %f" % (a, b, a-b))
    print("Kết quả %i x %i = %f" % (a, b, a*b))
    print("Kết quả %i / %i = %f" % (a, b, kq))





# Cách 2
try:
    a = 24
    b = int(input("Nhập số chia: "))
    kq = a/b
except ZeroDivisionError:
    print("Lỗi: b phải khác 0")
else:
    print("Kết quả %i + %i = %f" % (a, b, a+b))
    print("Kết quả %i - %i = %f" % (a, b, a-b))
    print("Kết quả %i x %i = %f" % (a, b, a*b))
    print("Kết quả %i / %i = %f" % (a, b, kq))