
from libs import my_lib

print(my_lib.f3())
print(my_lib.f4())




import libs.sub_libs.my_sub_lib
f5 = libs.sub_libs.my_sub_lib.f5()
print(f5)


from libs.sub_libs import my_sub_lib as mysublib
f6 = mysublib.f6()
print(f6)

# https://docs.python.org/3/library/