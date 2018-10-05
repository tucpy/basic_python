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

lst = [-4, -6, 2,5,6,9,12, 20, 23, 27, 33]

print("So nguyen to: ", So_nguyen_to(lst))

x = eval(input("nhap so: "))
print(type(x))