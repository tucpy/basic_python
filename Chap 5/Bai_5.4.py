

x = int(input('Nhập x: '))

count = 0
for i in range(1, x+1):
    if x % i == 0:
        count += 1

if count == 2:
    print('%i là số nguyên tố' %x)
else:
    print('%i không là số nguyên tố' %x)
