'''
def tinh_diem_tb(hk1, hk2):
    assert(hk1 >= 0 and hk2 >= 0), "Điểm hk1 và hk2 phải lớn hơn hoặc bằng 0"
    diem_tb = (hk1 + hk2 * 2) / 3
    return diem_tb

print(tinh_diem_tb(-2, 6.5))
'''
def is_prime(n):
    if 2 < n < 4:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
 
primes_under_100 = [p for p in range(2,101) if is_prime(p)]

print(primes_under_100)