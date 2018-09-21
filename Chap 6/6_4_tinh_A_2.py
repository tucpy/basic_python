import math

x = int(input("x: "))
n = int(input("n: "))

A = pow((x*x + x + 1),n) + pow((x*x-x+1),n)
print("A: ", A)