'''
Giai phuong trinh bac 2L ax^2 + bx + c = 0
Xet a, tinh delta, xet b
'''


import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))



if a == 0:
        if b == 0:
            if c != 0:
                print("Phuong trinh vo nghiem")
            else:
                print("Phuong trinh co vo so nghiem")
        else:
            x = -c/b
            print("Phuong trinh co nghiem x = %.2f" %x)

else:
    delta = pow(b,2) - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        x = -b/(2*a)
        print("Phuong trinh co nghiem kep: x1=x2= %.2f" %x)
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Phuong trinh co 2 nghiem x1= %.2f, x2=%.2f" %(x1,x2))