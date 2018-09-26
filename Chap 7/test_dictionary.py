


'''
dic1 = {"090909":"Nam", 2:"cat"}
str1 = str(dic1)
print(str1)
'''


'''
list1 = [i for i in range(1,11)]
tuple1 = tuple(list1)
print(tuple1)
dic_2 = dict.fromkeys(tuple1)
print(dic_2)
'''










Danh_sach_ban_be = {"01235468655": "Nguyễn Văn A", "0909090909": "Trần Thị B"}
# print(Danh_sach_ban_be)

tiep_tuc = True
while tiep_tuc:
    # Chọn chức năng
    chon = int(input("Bạn muốn làm gì? \n1. Xuất danh bạ \n2. Thêm mới \n3. Cập nhật danh bạ \n=> "))

    if chon == 1:
        # Xuất danh sách
        print("\nSĐT".ljust(20) + "HỌ TÊN".ljust(50))
        print("- "*25)
        for key in Danh_sach_ban_be:
            print(key.ljust(20) + Danh_sach_ban_be[key].ljust(50))

        tra_loi = input("Bạn có muốn tiếp tục nữa không (y/n)")
        if tra_loi == "y" or tra_loi == "Y":
            tiep_tuc = True
        else:
            tiep_tuc = False

    elif chon == 2:
        # Thêm mới
        sdt = input("Nhập sđt: ")
        if sdt in Danh_sach_ban_be:
            print("Đã tồn tại")
        else:
            hoTen = input("Họ tên: ")
            Danh_sach_ban_be[sdt] = hoTen



        # Tiếp tục ?
        tra_loi = input("\nBạn có muốn tiếp tục nữa không (y/n)")
        if tra_loi == "y" or tra_loi == "Y":
            tiep_tuc = True
        else:
            tiep_tuc = False

            # Xuất danh sách
            print("SĐT".ljust(20) + "HỌ TÊN".ljust(50))
            print("- "*25)
            for key in Danh_sach_ban_be:
                print(key.ljust(20) + Danh_sach_ban_be[key].ljust(50))
    
    elif chon == 3:
        # Cập nhật
        sdt = input("Nhập SĐT của bạn muốn thay đổi: ")
        if sdt in Danh_sach_ban_be:
            hoTen = input("Họ tên: ")
            Danh_sach_ban_be[sdt] = hoTen
        else:
            print("Số điện thoại không tồn tại")

        # Tiếp tục ?
        tra_loi = input("Bạn có muốn tiếp tục nữa không (y/n)")
        if tra_loi == "y" or tra_loi == "Y":
            tiep_tuc = True
        else:
            tiep_tuc = False

            # Xuất danh sách
            print("SĐT".ljust(20) + "HỌ TÊN".ljust(50))
            print("- "*25)
            for key in Danh_sach_ban_be:
                print(key.ljust(20) + Danh_sach_ban_be[key].ljust(50))

    else:
        print("Chỉ được nhập 1, 2 hoặc 3")
