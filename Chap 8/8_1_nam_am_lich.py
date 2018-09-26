

def tinh_can(nam):
    can = nam % 10
    if can == 0:
        tra_can = "Canh"
    elif can == 1:
        tra_can = "Tan"
    elif can == 2:
        tra_can = "Nham"
    elif can == 3:
        tra_can = "Quy"
    elif can == 4:
        tra_can = "Giap"
    elif can == 5:
        tra_can = "At"
    elif can == 6:
        tra_can = "Binh"
    elif can == 7:
        tra_can = "Dinh"
    elif can == 8:
        tra_can = "Mau"
    else:
        tra_can = "Ky"
    return(tra_can)


def tinh_chi(nam):
    chi = nam % 12
    if chi == 0:
        tra_chi = "Than"
    elif chi == 1:
        tra_chi = "Dau"
    elif chi == 2:
        tra_chi = "Tuat"
    elif chi == 3:
        tra_chi = "Hoi"
    elif chi == 4:
        tra_chi = "Ti"
    elif chi == 5:
        tra_chi = "Suu"
    elif chi == 6:
        tra_chi = "Dan"
    elif chi == 7:
        tra_chi = "Mao"
    elif chi == 8:
        tra_chi = "Thin"
    elif chi == 9:
        tra_chi = "Ty"
    elif chi == 10:
        tra_chi = "Ngo"
    else:
        tra_chi = "Mui"
    return(tra_chi)


nam = int(input("Nhap nam sinh: "))

print("Am lich: ", tinh_can(nam), tinh_chi(nam))
