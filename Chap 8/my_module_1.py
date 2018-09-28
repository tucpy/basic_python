import math

def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang / math.pow(chieu_cao,2)
    return bmi

def Loi_chao(ten):
    print("Xin chào bạn " + ten)

def Chao_mung(ten):
    print("Chào mừng " + ten + " đã tham gia")

def tong(a, b):
    return a + b

def hieu(a, b):
    return a - b

def checkprime(number):
    if number < 2:
        pass
    count = 0
    for i in range (1, number+1):
        if number % i == 0:
            count += 1
    return count == 2
        
                
            