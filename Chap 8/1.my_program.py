import my_module_1
import my_module



all_names = dir(my_module)
print(all_names)




# Tính BMI

bmi = my_module.tinh_bmi(50, 1.6)
print(bmi)


# Lời chào
'''
my_module.Loi_chao("Lan")
my_module.Chao_mung("Nam")
'''

# Tính tổng/hiệu
'''
from my_module import*

tong = tong(1,3)
print("Tổng:", tong)
hieu = hieu(9,4)
print("Hiệu:", hieu)

'''
