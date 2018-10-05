# Tạo list
def Tao_list(lst):
    i = 1
    while i == 1:
        gia_tri = int(input('Nhập giá trị: '))
        lst.append(gia_tri)
        i = int(input('Tiếp tục nhập giá trị? 1: Có, 0: không\t'))
    return lst

# Tính tổng các phần tử trong list


def Tinh_tong(lst):
    from functools import reduce
    from operator import add
    # Cách 1:
    # tong = reduce(lambda item1, item2: item1 + item2, lst)

    # Cách 2:
    tong = reduce(add, lst)
    return tong

# List số nguyên tố
def La_so_nguyen_to(n):
    if n < 2:
        return False
    else:
        # for i in range(2, n):
        #     if n % i == 0:
        #         return False
        # return True

        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        if count==2:
            return True
        else: 
            return False

def So_nguyen_to(lst):
    list_so_nguyen_to = list(filter(lambda x: La_so_nguyen_to(x), lst))
    return list_so_nguyen_to

# List các phần tử âm
def Phan_tu_am(lst):
    list_am = list(filter(lambda item: item < 0, lst))
    return list_am

# List các phần tử dương
def Phan_tu_duong(lst):
    list_duong = list(filter(lambda item: item > 0, lst))
    return list_duong


'''
list_so = []
list_so = Tao_list(list_so)
print(list_so)
'''

list_so = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# Tính tổng các phần tử trong list
# print("Tổng các phần tử trong list:", Tinh_tong(list_so))

# Tìm số nguyên tố
print("Danh sách số nguyên tố:", So_nguyen_to(list_so))