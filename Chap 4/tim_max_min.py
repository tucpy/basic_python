a = 3
b = 8
c = 7
d = 10

# Tìm max
# Đúng
so_max = a
if b > so_max:
    so_max = b

if c > so_max:
    so_max = c

if d > so_max:
    so_max = d
print("Max: ", so_max)

# Sai
'''
so_max = a
if b > so_max:
    so_max = b
elif c > so_max:
    so_max = c
else:
    so_max = d
print("Max: ", so_max)
'''


# Tìm min
so_min = a
if b < so_min:
    so_min = b
if c < so_min:
    so_min = c
if d < so_min:
    so_min = d
print("Min: ", so_min)