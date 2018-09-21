# Xét năm đó có là năm nhuần không?
# Năm nhuần là năm chia hết 4 và không chia hết cho 100
# Hay năm chia hết cho 400 cũng là năm nhuần

nam = int(input("Nhap so nam: "))

if (nam % 4 == 0 and nam % 100 !=0) or (nam % 400 == 0):
    print("Nam nhuan")
else:
    print("Khong phai nam nhuan")

