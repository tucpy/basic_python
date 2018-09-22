'''
danhSachPhim = ["Cuốn theo chiều gió",
                "Chiến tranh và hòa bình",
                "Titanic",
                "The bad, the good and the ugly",
                "Star war",
                "Iron man"]
       
        DANH SACH CAC FILM (6)
1. Cuốn theo chiều gió
2. Chiến tranh và hòa bình
3. Titanic
4. The bad, the good and the ugly
5. Star war
6. Iron man

'''
import string
danhSachPhim = ["Cuốn theo chiều gió",
                "Chiến tranh và hòa bình",
                "Titanic",
                "The bad, the good and the ugly",
                "Star war",
                "Iron man"]


print (("DANH SACH CAC FILM (%i)".center(50) %(len(danhSachPhim))))

#Cach 1:
for i in danhSachPhim:
    # print (danhSachPhim[i]) -> sai vi i luc nay la element chu ko phai index
    stt = danhSachPhim.index(i) #lay index cua list Phim
    print (str(stt+1) + ". " + i)

print()
#Cach 2:
n = len(danhSachPhim)
phim =""
for i in range(0,n):
    stt= i + 1
    phim = danhSachPhim[i]
    print(str(stt) + ". " + phim)

tiep_tuc = True


