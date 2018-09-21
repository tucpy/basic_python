'''
Nhap ho ten day du, tach ra ho, ten, tem dem
'''
import string
ho_ten = str(input("Ho ten: "))

cac_tu = ho_ten.split()
print (cac_tu)

ho = cac_tu[0]
print ("Ho: ", ho)

ten = cac_tu[len(cac_tu) - 1]
print ("Ten: ", ten)

chieu_dai = len(cac_tu)

ten_dem = ''

for i in range(1, (chieu_dai - 1) ):
    ten_dem += cac_tu[i] + ' '

print ("Ten dem: ", ten_dem)
    
