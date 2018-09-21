
a=int(input("Nhap vao so a: "))
b=int(input("Nhap vao so b: "))
c=int(input("Nhap vao so c: "))
d=int(input("Nhap vao so d: "))

print ("a , b , c , d = %d %d %d %d" %(a, b, c, d))

if a>b and a>c and a>d:
    print ("Max = %d" %(a))
elif b>a and b>c and b>d:
    print ("Max = %d" %(b))
elif c>a and c>b and c>d:
    print ("Max = %d" %(c))
else:
    print ("Max = %d" %(d))

if a<b and a<c and a<d:
    print ("Min = %d" %(a))
elif b<a and b<c and b<d:
    print ("Min = %d" %(b))
elif c<a and c<b and c<d:
    print ("Min = %d" %(c))
else:
    print ("Min = %d" %(d))


##Cach 2, gan so max vao a

a=int(input("Nhap vao so a: "))
b=int(input("Nhap vao so b: "))
c=int(input("Nhap vao so c: "))
d=int(input("Nhap vao so d: "))

print ("a , b , c , d = %d %d %d %d" %(a, b, c, d))

so_max = a
if b > so_max:
    so_max = b
if c > so_max:
    so_max = c
if d > so_max:
    so_max = d
print ("Max = %d" %(so_max))


so_min = a
if b < so_min:
    so_min = b
if c < so_min:
    so_min = c
if d < so_min:
    so_min = d
print ("Min = %d" %(so_min))


