
try:
    a = 24
    b = int(input("Nhập số chia: "))
    print("Kết quả %i : %i = %f:" % (a, b, a/b)) 
except ZeroDivisionError:
    print("Bạn phải nhập số chia khác 0")
finally:
    print("Kết quả %i + %i = %f:" % (a, b, a+b))
    print("Kết quả %i - %i = %f:" % (a, b, a-b))
    print("Kết quả %i x %i = %f:" % (a, b, a*b))