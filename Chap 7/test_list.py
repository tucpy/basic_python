'''
l1 = [1,2,3,4,5]
l2 = [3.6,5,7]
l3 = ["dog, cat"]
l4 = [1,5,3,[3,6]]
print(l1)
print(l2)
print(l3)
print(l4)
'''

'''
list6 = ["one", "two", "three", "four","five"]
print("Trước: ", list6)
del(list6[1])
print("Sau: ", list6)

print(list6[1:3])
'''


'''
so_lan = int(input("Bạn muốn nhập bao nhiêu số?\n=> "))
list_so = []
for i in range(1, so_lan + 1):
    so = int(input("Mời bạn nhập số thứ " + str(i) + ": "))
    list_so.append(so)
print(list_so)

tong = 0
for j in list_so:
    tong += j
trung_binh = tong / so_lan
print("Giá trị trung bình là:", round(trung_binh, 2))
'''


'''
l5 = [2,6,3,8,9]

tong = 0
for i in l5:
    # print(i)
    tong += i
print(tong)
'''

# print(max([1,2,3,4,5]))


'''
list_thu_cung = []
list_thu_cung.append("Dog")
list_thu_cung.append("Monkey")
print(list_thu_cung)
'''

'''
danhSachPhim = ["Cuốn theo chiều gió",
                "Chiến tranh và hòa bình",
                "Titanic",
                "The bad, the good and the ugly",
                "Star war",
                "Iron man"]

# In danh sách phim
n = len(danhSachPhim)
tieuDe = "DANH SÁCH CÁC PHIM (%i)" % n
print(tieuDe.center(50))

# Cách 1
for phim in danhSachPhim:
    stt = danhSachPhim.index(phim)
    print(str(stt+1) + ". " + phim)

print()

# Cách 2
phim = ""
for i in range(0, n):
    stt = i + 1
    phim = danhSachPhim[i]
    print(str(stt) + ". " + phim)
'''














