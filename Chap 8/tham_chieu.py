def change_list(lst):
    lst.append(100)
    lst.append(130)
    print("List trong hàm:", lst)
    return

lst = [1,3,7,12]
print(lst)

change_list(lst)

print("List ngoài hàm:", lst)