# Xét năm đó có là năm nhuần không?
# Năm nhuần là năm chia hết 4 và không chia hết cho 100
# Hay năm chia hết cho 400 cũng là năm nhuần

nam = int(input("Nhập năm: "))

if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print("Năm %i là năm nhuần" %nam)
else:
    print("Năm %i không là năm nhuần" %nam)