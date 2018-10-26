'''
In bang cuu chuong tu n den m
'''

n = int(input("Nhap n: "))
m = int(input("Nhap m: "))

if n < m:
    print("Tu cuu chung: %d" %n)
    print("Den cuu chuong: %d" %m)
    for i in range(n,(m+1)):
        for j in range(1,11):
            print("%i x %i = %i \t" %(i,j,i*j))
        print("\n")


    


