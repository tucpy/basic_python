# Viết hàm
def Giai_PT_Bac_Nhat(a, b):
    if a != 0:
        x = -b/a
        print("Nghiệm x =", x)
    elif b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")


# Main
a = -2
b = 9

Giai_PT_Bac_Nhat(a,b)


'''
#Bai tu lam
def phuong_trinh_bac_nhat(a,b):
    # ax + b = 0
    if (a == 0):
        print("Pt vo nghiem")
    else:
        x = -b/a
        print("Pt co nghiem x= ", x)

phuong_trinh_bac_nhat(1,4)

phuong_trinh_bac_nhat(0,10)
'''
