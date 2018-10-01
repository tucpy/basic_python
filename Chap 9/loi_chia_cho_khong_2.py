try:
    a = 24
    b = int(input("Nhập số chia: "))
    print("Kết quả %i / %i = %f" % (a, b, a/b))
except Exception as loi:
    print("Nhãn lỗi:", type(loi).__name__)  # nhãn lỗi
    print("Mô tả lỗi: " + format(loi))      # mô tả lỗi