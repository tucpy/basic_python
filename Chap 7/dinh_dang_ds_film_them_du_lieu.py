danhSachPhim = ["Cuốn theo chiều gió", 
                "Chiến tranh và hòa bình", 
                "Titanic", 
                "The bad, the good and the ugly", 
                "Star war", 
                "Iron man"]

tiep_tuc = True
while tiep_tuc:
    # Chọn chức năng
    chon = int(input("\nBạn muốn làm gì? \n1. Xuất thông tin phim \n2. Thêm phim mới \n"))

    if chon == 1:
        # In danh sách phim
        n = len(danhSachPhim)
        tieuDe = "DANH SÁCH CÁC PHIM (%i)" %n
        print(tieuDe.center(50))
        for phim in danhSachPhim:
            stt = danhSachPhim.index(phim)
            print(str(stt+1) + ". " + phim)

        tra_loi = input("\nBạn có muốn tiếp tục nữa không (y/n)")
        if tra_loi == "y" or tra_loi == "Y":
            tiep_tuc = True
        else:
            tiep_tuc = False

    elif chon == 2:
        # Thêm phim mới
        tenPhim = input("\nCho biết tên phim mới: ")
        danhSachPhim.append(tenPhim)

        # Tiếp tục ?
        tra_loi = input("\nBạn có muốn tiếp tục nữa không (y/n)")
        if tra_loi == "y" or tra_loi == "Y":
            tiep_tuc = True
        else:
            tiep_tuc = False

            # In danh sách phim
            n = len(danhSachPhim)
            tieuDe = "DANH SÁCH CÁC PHIM (%i)" %n
            print(tieuDe.center(50))
            for phim in danhSachPhim:
                stt = danhSachPhim.index(phim)
                print(str(stt+1) + ". " + phim)

    else:
        print("Chỉ được nhập 1 hoặc 2")