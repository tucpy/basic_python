import math

def Giai_PT_Bac_2(a,b,c):
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




a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

Giai_PT_Bac_2(a,b,c)



'''
#Bai tu lam

import math

def phuong_trinh_bac_hai(a,b,c):
    if (a == 0):
        if b == 0:
            if c != 0:
                print("Phuong trinh vo nghiem")
            else:
                print("Phuong trinh co vo so nghiem")
        else:
            x = -c/b
            print("Phuong trinh co nghiem: x=", x)
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            print("Phuong trinh vo nghiem")
        elif delta ==0:
            x = -b/2*a
            print("Phuong trinh co nghiem kep: x= ", x)
        else:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            print("Phuong trinh co 2 nghiem phan biet")
            print("x1: ", x1)
            print("x2: ", x2)


phuong_trinh_bac_hai(1,3,5)

phuong_trinh_bac_hai(3,10,5)

phuong_trinh_bac_hai(0,2,6)

phuong_trinh_bac_hai(0,0,6)

'''

'''
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
'''