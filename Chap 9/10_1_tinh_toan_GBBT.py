'''
Tinh bieu thuc A
Bo sung ngoai le: x, y>0
'''

import math

def tinhGTBT(x,y):
    try:
        #x = int(input("Nhap x: "))
        #y = int(input("Nhap y: "))
        
    except ZeroDivisionError:
        print("Ban phai nhap so chia lon hon 0")
    finally:
        A = math.sqrt((5*x -y) / ((2*x) + (7*y)))
        return A


print(tinhGTBT(2,5))



