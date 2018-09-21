# S = (x^2 + 1)^n

n = int(input('Nhập n: '))
x = float(input('Nhập x: '))

if n == 0:
    S = 1
    print(S)
else:
    S = 1

    # Dùng for
    for i in range(1, n+1):
        S = S * (x * x + 1)
        print(S)
    print('S = (x*x + 1)^n=', S)


    # Dùng while
    '''
    i = 1
    while i <= n:
        S = S * (x * x + 1)
        i += 1
    '''

    S = pow((x * x + 1), n)
    print('S = (x*x + 1)^n=', S)
    