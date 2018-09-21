tiep_tuc = True

while tiep_tuc:
    chon_hinh = int(input("Bạn muốn in hình gì?\n 1. Hình chữ nhật\n 2. Hình tam giác\n=> "))
    # In hình chữ nhật
    if chon_hinh == 1:
        dai = int(input("Nhập chiều dài: "))
        rong = int(input("Nhập chiều rộng: "))
        i = 1
        while i <= rong:
            print("*  " * dai)
            i += 1

    # Tam giác
    elif chon_hinh == 2:
        n = int(input("Nhập vào chiều dài 1 cạnh: "))
        i = 1
        while i <= n:
            print("*  " * i)
            i += 1
    
    # Thông báo nhập khác 1 hoặc 2
    else:
        print("Chỉ chọn 1 hoặc 2")


    # Tiếp tục in nữa hay không ?
    chon = input("Bạn có muốn in tiếp không? (y/n)\n=> ")
    if chon == "y" or chon == "Y":
        tiep_tuc = True
    else:
        tiep_tuc = False