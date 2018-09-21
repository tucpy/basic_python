'''
Tinh S = ((x^2) + 1)^n
'''

n = int(input("Nhap n: "))
x = float(input("Nhap x: "))

S = 1
for i in range (1, n+1):
    S = S * (x*x + 1)

print("S: ", S)