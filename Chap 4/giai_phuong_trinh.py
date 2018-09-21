
#Giai phuong trinh ax + b = 0


a=int(input("Nhap vao so a: "))
b=int(input("Nhap vao so b: "))

if a != 0:
    x=-b/a
    print ("Phuong trinh co 1 nghiem: %d" %(x))
else:
    if b == 0:
        print ("Phuong trinh co vo so nghiem")
    else:
        print ("Phuong trinh vo nghiem")