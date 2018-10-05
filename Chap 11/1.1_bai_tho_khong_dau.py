
# Đọc bài thơ

f = open("1.1_bai_tho_khong_dau.txt", "r")
noi_dung = f.read(10)
print(noi_dung)
f.close()


'''
# Ghi mới / tiếp theo
f = open("1.1_bai_tho_khong_dau.txt", "a+")
noi_dung = "\n\nBuoc toi deo ngang bong xe ta"
noi_dung += "\nCo cay chen da, la chen hoa"
noi_dung += "\nLom khom duoi nui tieu vai chu"
noi_dung += "\nLac dac ben song cho may nha"
f.write(noi_dung)
f.close()
'''