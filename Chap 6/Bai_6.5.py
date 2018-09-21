import math

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

# Phương trình bậc nhất
if a == 0:
    if b!=0:
        x = -c/b
        print("Phương trình có 1 nghiệm %i" %x)
    else:
        if c==0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")

# Phương trình bậc 2
else:
    delta = math.pow(b, 2) - 4*a*c
    # delta = b*b - 4*a*c
    if delta == 0:
        x = -b/(2*a)
        print("Phương trình có 1 nghiệm duy nhất x =", x)
    elif delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Phương trình có 2 nghiệm phân biệt")
        print("x1 =", x1)
        print("x2 =", x2)
    else:
        print("Phương trình vô nghiệm")