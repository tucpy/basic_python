'''
Nhap list co cac con thu. Nhap mot con thu can tim
Viet chuong trinh in danh sach thu, so luong thu va ket qua tim kiem

'''

animal = ['ant', 'bear','cat','dog','elephant','fish', 'goat', 'hippo']
find = str(input("I want to find: "))

print ("Number of animal: ", len(animal) )

if find in animal:
    print ("There is", find,"in list of animals")
else:
    print (find,"is not in list of animals")
