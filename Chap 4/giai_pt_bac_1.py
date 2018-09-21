# Giải phương trình bậc nhất ax + b = 0

a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))


if a!=0:
    x = (-b)/a
    print("Phương trình có 1 nghiệm %i" %x)
else:
    if b==0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")


'''
if a!=0:
    x = (-b)/a
    print("Phương trình có 1 nghiệm %i" %x)
elif a==0 and b == 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Phương trình vô nghiệm")
'''