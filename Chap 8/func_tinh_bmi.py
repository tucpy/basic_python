import math

def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang / math.pow(chieu_cao,2)
    print(bmi)
    return bmi

tinh_bmi(56, 1.65)

#kq = tinh_bmi(56,1.65)
#print(kq)