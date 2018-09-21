x= 0

c = int(input("Nhap bang cuu chuong: "))

'''
while x<=10:
    t = x * c
    print("%i * %i = %i" %(x,c,t))
    x += 1
'''

for x in range(0,11):
    t = x * c
    print("%i * %i = %i" %(x,c,t))
    #x += 1 (khong can vi x tu tang trong vong lap for)