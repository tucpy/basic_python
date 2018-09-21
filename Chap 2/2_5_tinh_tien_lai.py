laisuat = float(input("Lai suat 1 nam (%): "))

tiengui = float(input("So tien gui: "))

sothang = float(input("So thang gui: "))

tienlai = (tiengui*sothang) * (laisuat/100/12)
tongtien = tiengui + tienlai

print ("Tien lai %.1f" %(tienlai))
print ("Tong tien %i" %(tongtien))