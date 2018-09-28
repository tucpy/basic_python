# basic_python
Chapter 7: List - Tuple - Set - Dictionary
Mục tiêu chính:
- List 
- Tuple
- Set
- Dictionary

Các kiểu cấu trúc dữ liệu trong Python:

1. List: cấu trúc dữ liệu cơ bản thuộc nhóm Sequence.
+ Gồm nhiều phần tử (n), mỗi phần tử có 1 vị trí index, chạy từ 0 đến (n-1)
+ Các phần tử có thể cùng hoặc khác kiểu. Cùng kiểu thì dễ xử lý tính toán

list1 = ['spring', 'summer', 'fall', 'winter'] # khởi tạo list

print (list1[1]) # -> summer. Truy xuất phần tử trong list theo index

list1[1] = 'nothing' # cập nhật giá trị cho phần tử trong list

del(list[1]) # xoá phần tử trong list

len(list1) # chiều dài của list (số phần tử trong list)

list_new = list1 + list2 + list3 # tạo list mới bằng cách nối các list với nhau

list_new = list1 * 3 # tạo list mới bằng cách lặp lại các list đã có

list_new = list1[2:] # tạo list mới bằng cách copy phần tử từ vị trí index đến cuối list

"fall" in list1 # -> True. Tìm kiếm giá trị trong list, trả về True or False

for item in list_new: 
	print(item)  # duyệt list, xử lý hiển thị hoặc tính toán các phần tử

list1[0] # -> 'spring'
list1[-1] # ->'winter' truy xuất giá trị của các phần tử trong list tại vị trí index

list_so = [-4, 2, 6, 9]
max(list_so) #-> 9  
min(list_so) #-> -4

list_so.append(20) # -> list_so[-4, 2, 6, 9, 20]

list_so.count(6) # ->1. Đếm số lần xuất hiện của element trong list

small_list = [1, 2, 3]
large_list = [4, 5, 6]
large_list.extend(small_list)
print (large_list) # -> [4, 5, 6, 1, 2, 3], mở rộng list

all_list = ['one', 'two', 'three', 'abc', 1, 2, 3]
all_list.index('abc') # -> 3 , tìm index của element trong list, nếu ko tìm thấy sẽ báo lỗi

all_list.insert(2, 'elephant')
print(all_list) #-> ['one', 'two', 'elephant', 'three', 'abc', 1, 2, 3]

all_list.pop() #-> 3, lấy phần tử cuối
all_list.pop(2) #-> 'elephant'

all_list.remove('three') #xoá phần tử ra khỏi list

all_list.reverse() # đảo ngược list

large_list.sort() # sắp xếp theo giá trị tăng dần

2. Tuple: cấu trúc dữ liệu cơ bản thuộc nhóm Sequence.
+ Giới hạn, cố định số phần tử (n), không được thay đổi giá trị phần tử
+ Index từ 0 đến n-1

tup1 = ('one', 'two', 'three', 'four')
tup1[2] # ->'three'
tup1[1:3] # -> 'two', 'three'. từ begin đến (end - 1)
del(tup1) # xoá bỏ cả tuple (vì ko thể thay đổi tuple)

# các phương thức truy xuất tương tự list, tuy nhiên ko có 
# sort, reverse, remove, pop, insert, extend, append

tup_copy = tuple(list1) # copy các phần tử trong list1 vào tuple_copy



3. Dictionary

4. Set
  










Bài tập:
1. Bài 7_1_list_of_animals.py
2. Bài 7_2_list_number_1.py
3. Bài 7_3_list_number_2.py
4. Bài 7_4_tuples_strings.py
5. Bài 7_5_tuple_numbers.py
6. Bai 7_6_set_numbers.py
7. Bai 7_7_danh_ba.py
8. Bai 7_8_tu_dien.py
