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

list1 = [i for i in range(1,11) if i%2==0] # chỉ lấy số chẵn

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

str1 = "abc"
str2 = list(str1)
print str2 #-> ["a","b","c"]

3. Dictionary: cấu trúc dữ liệu cơ bản thuộc nhóm Sequence.
+ Gồm nhiều phần tử, mỗi phần tử là một bộ key : value
+ Key là duy nhất trong dictionary, còn value thì có thể trùng
+ Kiểu dữ liệu có thể là string, number hoặc tuple

+ Tạo dictionary:
dic1 = {1: "one", 2: "two", 3:"three", 4: "four"}
print (dic1) # -> {1:'one', 2:'two', 3:'three', 4:'four'}

+ Truy xuất giá trị trong dictionary: tên dictionary[key]
print (dic1[1]) #-> 'one'

+ Cập nhật giá trị trong dictionary:
tên dictionary [key] = value # nếu key cũ, chỉ cập nhật giá trị của key
tên dictionary [key] = value # nếu key mới, thêm phần tử mới

+ Xoá phần tử trong dictionary:
xoá theo khoá: del ten_dictionary[key]
xoá tất cả phần tử: ten_dictionary.clear()
xoá cả dictionary: del ten_dictionary

Note: key là duy nhất trong dictionary, ko có key trùng nhau
Key có giá trị ko thay đổi, do đó chỉ có thể cập nhật value, ko thể cập nhật key

len(tên dictionary) # chiều dài của dictionary
str(tên dictionary) # in dictionary dưới dạng chuỗi
dict1_copy = dic1.copy() # tạo bản sao của dict1


4. Set: cấu trúc dữ liệu cơ bản thuộc nhóm Sequence.
+ Mỗi phần tử trong set là duy nhất, không có 2 phần tử trùng nhau, và giá trị của phần tử không thay đổi.
+ Các phần tử trong set ko theo thứ tự thêm vào, không sử dụng index

+ Khởi tạo set:
set1 = {1, 3, 5, 7}
set_string = { "a", "b", "c"}

+ Khởi tạo set ban đầu chưa có phần tử:
set_fruits = set()

+ Cập nhật giá trị/ thêm mới:
set_fruits.add("orange")

+ Xoá phần tử trong set:
set_fruits = {"orange","banana","apple","grape","kiwi"}

set_fruits.discard("appple")  # nếu ko tìm thấy trong set sẽ ko xoá và ko báo lỗi
set_fruits.remove("straberry") # nếu ko tìm thấy trong set sẽ báo lỗi

+ Xoá toàn bộ element trong set
set_fruits.clear()

del(set_fruits) # xoá luôn set

+ Lấy element ra khỏi set: kết quả trả về là element được pop, báo lỗi nếu set ko có element nào
set_fruits.pop()

+ Các phương thức cơ bản:

len, max, min, sum:
set_dest = {1, 2, 3, 4, 5}
len(set_dest)
max(set_dest)
min(set_dest)
sum(set_dest)

set_copy = set_dest.copy()

+ Duyệt set (như duyệt list)
for item in set_dest:
	print("Item:", item)

+ Set union: trả về tất cả các element ko trùng nhau của các set
setA = {1, 2, 6, 3, 7}
setB = {1, 4, 5, 8, 9}
setC = setA | setB
print(setC)
{1, 2, 3, 4, 5, 6, 7, 8, 9}

+ Set intersection: trả về tất cả các element cùng xuất hiện trong các set
setD = setA & setB
print(setD)
{1}

+ Set difference: trả về các element chỉ có trong set này mà ko có trong set kia
set_difference = set1 - set2
setE = setA - setB
print(setE)
{2, 3, 6, 7}

+ Set symmetric difference: trả về các element ko cùng xuất hiện trong các set
set_symmetric_difference = set1 ^ set2
setF = setA ^ setB
print(setF)

+ sắp xếp set tăng dần, giảm dần:
tăng: sorted(tên set)
giảm: sorted(tên set, reverse = True)








Bài tập:
1. Bài 7_1_list_of_animals.py
2. Bài 7_2_list_number_1.py
3. Bài 7_3_list_number_2.py
4. Bài 7_4_tuples_strings.py
5. Bài 7_5_tuple_numbers.py
6. Bai 7_6_set_numbers.py
7. Bai 7_7_danh_ba.py
8. Bai 7_8_tu_dien.py
