# Nhập a,b,c là chiều dài các cạnh của 1 tam giác
# Xét a,b,c có thỏa điều kiện của tam giác?
# (a + b) > c và (a + c) > b và (b + c) > a

a = int(input("Nhap canh a: "))

b = int(input("Nhap canh b: "))

c = int(input("Nhap canh c: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print ("Day la tam giac")
else:
    print ("Day khong phai tam giac")
