n = int(input('Nhập n: '))


A = 0
chuoi_A = ''

B = 0
chuoi_B = ''

C = 1
chuoi_C = ''

D = 1
chuoi_D = ''

E = 0
chuoi_E = ''


i = 1
while i<=n:
    # Tính A
    if i%2!=0:
        A = A + i
        chuoi_A = chuoi_A + str(i) + ' + '
    
    # Tính B
    if i%2==0:
        B = B + i
        chuoi_B = chuoi_B + str(i) + ' + '
    
    # Tính C
    C = C * i
    chuoi_C = chuoi_C + str(i) + ' * '

    # Tính D
    if i%3==0:
        D = D * i
        chuoi_D = chuoi_D + str(i) + ' * '

    # Tính E
    count = 0
    for j in range(1, i+1):
        if i%j == 0:
            count = count + 1

    if count == 2:
        E = E + i
        chuoi_E = chuoi_E + str(i) + ' + '
    i = i + 1

# In kết quả
print('A =', chuoi_A, '=', A)
print('B =', chuoi_B, '=', B)
print('C =', chuoi_C, '=', C)
print('D =', chuoi_D, '=', D)
print('E =', chuoi_E, '=', E)