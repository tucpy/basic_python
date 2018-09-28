day_so = [-4, -7, -2, 3, 5, 9, 18]
so_nguyen_to =[i for i in day_so if (all(i % j != 0 for j in range(2, i)))]
print(so_nguyen_to)

so_nguyen_to1 =[i for i in day_so if (i % j != 0 for j in range(2, i))]
print(so_nguyen_to1)

day_x = [-4, -7, -2, 3, 5, 9, 18]
so = []
for l in day_x:
    for k in range (2,l):
        if l % k != 0:
            so.append(l)
print("so nguyen to: ", so)