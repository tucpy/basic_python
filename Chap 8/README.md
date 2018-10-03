# basic_python
Chapter 8: Function
Mục tiêu chính:
- Xay dung va goi su dung phuong thuc/ham

1. Function:

+ function là tập hợp các dòng code được viết để thực hiện một chức năng nào đó
+ Mục đích xây dựng function là để tái sử dụng khi cần

+ Cú pháp: 
def function_name(parameters):
    #mô tả về function
    các dòng lệnh
    return [expression]

+ Gọi function:
function_name(values)

+ Local var: có thể được truy cập chỉ trong function mà chúng được khai báo
+ Global var: có thể được truy cập trên toàn chương trình của tất cả các function

+ Tham số (parameter/argument): tham chiếu (reference) hay tham trị (value)

Các tham số (parameter/argument) có kiểu tham trị trong function: nếu thay đổi giá trị của nó trong function thì ko ảnh hưởng gì đến giá trị của nó ở ngoài function
Các tham số (parameter/argument) có kiểu tham chiếu trong function: nếu thay đổi giá trị của nó trong function thì cũng sẽ thay đổi giá trị của nó bên ngoài function

+ Ví dụ tham trị:

def tinh_binh_phuong(so):
    # tinh binh phuong cua mot so
    so = so * so
    print("So in function = ", so)

>>> so = 8
>>> tinh_binh_phuong(so)
So in function = 64
>>> print("So out function = ", so)
So out function = 8 

+ Vi dụ tham chiếu:
def change_list(lst):
    # them vao sau list
    lst.append(10)
    lst.append(20)
    print("List in function: ", lst)
    return

>>> lst = [1, 3, 7, 12]
>>> print("List: ", lst)
List: [1, 3, 7, 12]
>>> change_list(lst)
List in function: [1, 3, 7, 12, 10, 20]
>>> print("List now: ", lst)
List now: [1, 3, 7, 12, 10, 20]

+ Tham số: có 4 loại:
+ Required argument (tham số bắt buộc): truyền giá trị vào phải đúng vị trí theo qui định
+ Keyword argument (tham số từ khoá): ko cần theo vị trí, nhưng giá trị phải đi kèm từ khoá
+ Default argument (tham số mặc định): tự động lấy giá trị mặc định nếu người dùng ko cung cấp giá trị
+ Variable-length argument (tham số có chiều dài thay đổi ko xác định): sủ dụng khi chưa xác định được số các giá trị truyền vào function.
*parameter_name. Chỉ có 1 tham số loại này trong function và nó phải đứng sau cùng

def in_loi_chao (loi_chao, *danh_sach_ten);
    #in loi chao theo danh sach ten
    for ten in danh_sach_ten:
        print(loi chao, ten)
    return

in_loi_chao("Hello", "An", "Huy", "Hong")

2. Anonymous Function (lambda)

+ Gọi là phương thức ẩn danh vì nó ko được khai báo theo các tiêu chuẩn bằng từ khoá def mà được viết ngắn gọn bằng cách sử dụng từ khoá lambda để tạo ra các phương thức ngắn (1 dòng lệnh)

Cú pháp: lambda[parameter 1, parameter 2]: expression

Chú ý: 
+ Lambda có thể có 1 hoặc nhiều tham số truyền vào nhưng chỉ trả về 1 giá trị duy nhất
+ Lambda ko thể chứa nhiều command hoặc expression
+ Lambda ko thể được gọi trực tiếp để in kết quả vì nó yêu cầu 1 expression
+ Lambda có local namespace của nó và ko thể truy cập các biến khác và biến trong phạm vi global namespace

Ví dụ:

import math
# tinh S = (x*x + 1)^ n
s = lambda x, n: math.pow(math.pow(x,2) + 1, n)

3. Built-in Function

map(), reduce(), filter() hỗ trợ việc xử lý các sequence









Bài tập:
1. 8_1_nam_am_lich.py
2. 8_2_tinh_BMI
3. 
4. 
5. 
6. 
7. 
8. 
