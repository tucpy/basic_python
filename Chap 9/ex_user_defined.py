class Loi_nhap_lieu(ValueError):
    def __init__(self, thong_bao):
        self.thong_bao = thong_bao


try:
    a = 24
    b = int(input("Nhập số chia: "))
    if b == 0:
        raise Loi_nhap_lieu("Lỗi chia cho 0")
    else:
        print("Kết quả %i : %i = %f" % (a, b, a/b))
except Loi_nhap_lieu as ex:
    print(ex.thong_bao)
finally:
    print("Kết quả %i + %i = %f" % (a, b, a+b))
    print("Kết quả %i - %i = %f" % (a, b, a-b))
    print("Kết quả %i x %i = %f" % (a, b, a*b))

# https://docs.python.org/3/library/exceptions.html