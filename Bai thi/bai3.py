
tiep_tuc = True

tong_tien = 0

tieu_de = "LICH SU GIAO DICH"
lich_su =[]

while tiep_tuc:
    # Chon chuc nang:
    chon = int(input(("Ban muon lam gi?\n 1. Gui tien \n 2. Rut tien\n Vui long chon: ")))
    if chon == 1:
        tien_gui = int(input("Ban muon gui bao nhieu tien: "))
        while tien_gui < 0:
            tien_gui = int(input("Vui long nhap so duong: "))
        tong_tien += tien_gui
        lich_su.append(tien_gui)
       
        # in lich su giao dich
        print (tieu_de.center(50,'-'))
        for i in range(0, len(lich_su)):
            print("{:,}".format(lich_su[i]), "VND")
        print ("\n\n TONG TIEN:", "{:,}".format(tong_tien), "VND")
       
        # tiep tuc
        tra_loi = input("\nBan co muon thuc hien giao dich nao khac nua khong (y/n)?")
        if tra_loi == "y" or tra_loi == "Y":
            tiep_tuc = True
        else:
            tiep_tuc = False
    
    elif chon == 2:
        tien_rut = int(input("Ban muon rut bao nhieu tien: "))
        if ((tong_tien == 0) or (tien_rut > tong_tien)):
            print("So tien trong tai khoan khong du")
        else:
            tong_tien -= tien_rut
            lich_su.append(-tien_rut)
            print (tieu_de.center(50,'-'))
            for i in range(0, len(lich_su)):
                print("{:,}".format(lich_su[i]), "VND")
            print ("\n\n TONG TIEN:", "{:,}".format(tong_tien), "VND")
        
        # tiep tuc
        tra_loi = input("\nBan co muon thuc hien giao dich nao khac nua khong (y/n)?")
        if tra_loi == "y" or tra_loi == "Y":
            tiep_tuc = True
        else:
            tiep_tuc = False
    
    else:
        print("Chi duoc nhap 1 hoac 2")


