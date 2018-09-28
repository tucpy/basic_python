import math

# Hình tròn
chu_vi_hinh_tron = lambda r: r * 2 * math.pi
dien_tich_hinh_tron = lambda r: math.pi * math.pow(r,2)

r = 10
print('Chu vi hình tròn =', chu_vi_hinh_tron(r))
print('Diện tích hình tròn =', dien_tich_hinh_tron(r))


# Hình chữ nhật
chu_vi_hinh_chu_nhat = lambda dai, rong: 2 * (dai + rong)
dien_tich_hinh_chu_nhat = lambda dai, rong: dai * rong

dai = 5
rong = 3
print('Chu vi hình chữ nhật =', chu_vi_hinh_tron(r))
print('Diện tích hình chữ nhật =', dien_tich_hinh_tron(r))