'''
# In các phần tử trong vòng lặp
for i in range(1, 11):
    print("i =", i)


# Tính tổng các phần tử chẵn
tong = 0
for i in range(1, 11):
    if i % 2 == 0:
        tong = tong + i
print(tong)
'''

# In bảng cửu chương
cuu_chuong = int(input("Nhập cửu chương: "))
for i in range(1, 11):
    print("%i x %i = %i" %(i, cuu_chuong, i*cuu_chuong))
else:
    print("Kết thúc cửu chương", cuu_chuong)