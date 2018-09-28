import math
def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang / pow(chieu_cao,2)
    return bmi

def danh_gia_bmi(bmi):
    if bmi < 18.5:
        print("Ban hoi gay")
    elif bmi >= 18.5 and bmi < 25:
        print("Ban binh thuong")
    else:
        print("Ban thua can")


can_nang = float(input("Nhap can nang (kg): "))
chieu_cao = float(input("Nhap chieu cao (m): "))
bmi = tinh_bmi(can_nang, chieu_cao)
print(bmi)
danh_gia_bmi(bmi)
