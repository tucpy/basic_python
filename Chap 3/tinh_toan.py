# Viết chương trình nhập hai số nguyên x, y
# Tính: p=x*y, s=x+y, A=s^2+p(s-x)*(p+y) và in kết quả.

x = int(input("x: \t"))
y= int(input("y: \t"))

p= x * y

s= x + y

A = (s^2 + p*(s-x) * (p+y))

print ("p=",p)
print ("s=",s)
print ("sum=", A)