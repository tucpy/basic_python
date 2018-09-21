'''
# In các phần tử trong vòng lặp

x = 1
while x <= 10:
    print("x =", x)
    x += 1



# Tính tổng các phần tử trong vòng lặp
x = 11
tong = 0
while x <= 10:
    tong = tong + x
    x += 1

print("Tổng các phần tử:", tong)
'''


# In bảng cửu chương
cuu_chuong = int(input("Nhập vào cửu chương: "))
i = 1
while i<=10:
    print("%i x %i = %i" %(i, cuu_chuong, i*cuu_chuong)) 
    i += 1
else:
    print("Kết thúc cửu chương", cuu_chuong)