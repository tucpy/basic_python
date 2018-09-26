'''
Danh_sach_ban_be = {"01235468655": "Nguyễn Văn A", "0909090909": "Trần Thị B"}
print(Danh_sach_ban_be)

# DS bạn bè
def In_danh_ba():
    print('Danh bạ điện thoại:')
    print('Tên \t Số điện thoại')
    for key, value in Danh_sach_ban_be.items():
        print(key, ' -- ', value)


# Thêm mới
def Them_danh_ba():
    sdt = input("Nhập SĐT: ")
    if sdt not in Danh_sach_ban_be:
        hoTen = input("Họ tên: ")
        Danh_sach_ban_be[sdt] = hoTen
        #print(Danh_sach_ban_be)
    else:
        print("Đã có bạn ")



# Thay đổi
def Thay_doi_danh_ba():
    sdt = input("Nhập SĐT của bạn muốn thay đổi: ")
    if sdt in Danh_sach_ban_be:
        hoTen = input("Họ tên: ")
        Danh_sach_ban_be[sdt] = hoTen
        #print(Danh_sach_ban_be)
    else:
        print("Số điện thoại không tồn tại")





tiep_tuc = True
while tiep_tuc:
    # Chọn chức năng
    chon = int(input("Bạn muốn làm gì? \n1. Xuất danh bạ \n2. Thêm mới \n3. Cập nhật danh bạ \n=> "))

    if chon == 1:
        # Xuất danh sách
        In_danh_ba()

        tra_loi = input("Bạn có muốn tiếp tục nữa không (y/n)")
        if tra_loi == "y" or tra_loi == "Y":
            tiep_tuc = True
        else:
            tiep_tuc = False

    elif chon == 2:
        # Thêm mới
        Them_danh_ba()

        # Tiếp tục ?
        tra_loi = input("\nBạn có muốn tiếp tục nữa không (y/n)")
        if tra_loi == "y" or tra_loi == "Y":
            tiep_tuc = True
        else:
            tiep_tuc = False

            # Xuất danh sách
            In_danh_ba()
    
    elif chon == 3:
        # Cập nhật
        Thay_doi_danh_ba()

        # Tiếp tục ?
        tra_loi = input("Bạn có muốn tiếp tục nữa không (y/n)")
        if tra_loi == "y" or tra_loi == "Y":
            tiep_tuc = True
        else:
            tiep_tuc = False

            # Xuất danh sách
            In_danh_ba()

    else:
        print("Chỉ được nhập 1, 2 hoặc 3")

'''




'''
print("Giả lập thực đơn.")
tiep_tuc = True
while tiep_tuc:
    print("Thực đơn".center(30, " "))
    print("* "*15)
    print("1. In danh sách bạn bè.")
    print("2. Thêm bạn bè.")
    print("3. Cập nhật bạn bè.")
    print("4. Thoát.")
    print("* "*15)
    chon = int(input("Mời bạn chọn: "))
    if chon == 1:
        In_danh_ba()
    elif chon == 2:
        Them_danh_ba()
        In_danh_ba()
    elif chon == 3:
        Thay_doi_danh_ba()
        In_danh_ba()
    elif chon == 4:
        tiep_tuc = False
    else:
        print("Bạn chỉ chọn 1,2,3,4")
'''

'''
def in_loi_chao(loi_chao, a, *danh_sach_ten):
    for ten in danh_sach_ten:
        print(loi_chao, a, ten)


in_loi_chao("Hello", "Lan", "Mai", "Đào")
'''