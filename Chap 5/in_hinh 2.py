tiep_tuc = True

while tiep_tuc:
    chon_hinh = int(input("Ban muon in hinh gi?\n 1. Hinh chu nhat\n 2. Hinh tam giac\n"))
    #In hinh chu nhat
    if chon_hinh == 1:
        dai = int(input("Nhap chieu dai: "))
        rong = int(input("Nhap chieu rong: "))
        i = 1
        while i <= rong:
            print("* " * dai)
            i +=1
    #In hinh tam giac
    elif chon_hinh == 2:
        n = int(input("Nhap chieu dai 1 canh: "))
        i = 1
        while i <= n:
            print("* " * i)
            i += 1

    else:
        print("Chi chon 1 hoac 2")

chon = input("Ban co muon in tiep ko? (y/n)\n => ")
if chon == "y" or chon =="Y":
    tiep_tuc = True
else:
    tiep_tuc = False
