'''
Created on Oct 3, 2018

@author: lntri
'''
# https://www.tutorialspoint.com/python3/python_files_io.htm

f = open("1.1_bai_tho_khong_dau.txt", "rb")
noi_dung = f.read(12)
print(noi_dung)
'''
# Kiểm tra trạng thái đóng/mở của file
if f.closed == "True":
    print("Trạng thái: File đã đóng")
else: print("Trạng thái: File đang mở")

# Kiểm tra mode file
mode_file = f.mode
print("Mode của file:", mode_file)

# Tên file:
file_name = f.name
print("Tên file:", file_name)
'''

# tell
pos_tell = f.tell()
print("Vị trí hiện tại:", pos_tell)


# seek
pos_seek = f.seek(3,1)
print(pos_seek)
