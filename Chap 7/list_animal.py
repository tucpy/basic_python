# Viết chương trình cho người dùng nhập vào các chuỗi. 
# Khi nào người dùng muốn dừng lại thì bấm 1 phím nào đó (do người lập trình chọn)
# Khi chương trình dừng lại sẽ in ra màn hình danh sách các chuỗi đã nhập theo thứ tự tăng dần
# Ví dụ người dùng nhập: [dog, cat, elephant, lion, fish]
# Xuất ra màn hình: ['cat', 'dog', 'elephant', 'fish', 'lion']


tiep_tuc = True
danh_sach =[]
while tiep_tuc:
    chuoi = str(input("Moi ban nhap chuoi (neu dung lai bam phim s): "))

    # Cach nay se ko dung vong lap duoc
    #if chuoi !='s' or chuoi !='S':
        #danh_sach.append(chuoi)
    #else:
        #tiep_tuc = False
    # Cach nay moi dung
    if chuoi =='s' or chuoi =='S':
        tiep_tuc = False
    else:
        danh_sach.append(chuoi)

#sort cac phan tu theo thu tu tang dan
danh_sach.sort()
#in danh sach da sap xep
print(danh_sach)


