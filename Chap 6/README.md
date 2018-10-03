# basic_python
Chapter 6: Numbers - Strings - Datetimes
Mục tiêu chính:
- Các hàm thư viện Numbers - Strings - Datetimes

1. Numbers:
+ Tính toán: (import math)

abs(x) #|x|
ceil(x) #giá trị nguyên nhỏ nhất lớn hơn x (làm tròn lên số nguyên gần nhất)
exp(x) #e^x
fabs(x) #|x| (float abs)
floor(x) #giá trị nguyên lớn nhất nhỏ hơn x (làm tròn xuống số nguyên gần nhất)
log(x)
max(x1, x2...)
min(x2, x2...)
modf(x) #tách x thành 2 phần: phần lẻ và phần nguyên, kết quả trả về đều là kiểu float
pow(x,y) #x^y
round(x1,[,n]) # làm tròn, với n số lẻ
sqrt(x)

+ Tạo số ngẫu nhiên: (import random)
random.randrange (0, 20, 2) # số ngẫu nhiên trong khoảng 0-20, step là 2
random() # số thực ngẫu nhiên trong khoảng >0 và <1
uniform(x,y) # số thực ngẫu nhiên trong khoảng >x và <y

2. Strings:


capitalize() # str = "happy birthday", str.capitalize() -> "Happy Birthday"

center(width, fillchar) # canh giữa, điền vào đầu và cuối chuỗi kí tự fillchar, mặc định là điền khoảng trắng

ljust() # canh trái
rjust() # canh phải
upper() # viết hoa toàn bộ

count(sub, [start,end]) # số lần chuỗi con xuất hiện trong chuỗi chính, tính từ start đến end

find(str2, [beg, end]) # tìm str2 từ vị trí beg đến end, trả về vị trí nếu tìm thấy, -1 nếu ko tìm thấy. 
Mặc định beg=0 và end=len

isdigit() # nếu chỉ chứa số -> true
replace(old, new, [max]) # thay old bằng new, nếu có max thì chỉ thay 1 lần
strip([chars]) # bản sao sau khi loại bỏ chars ở đầu và cuối chuỗi, mặc định là loại bỏ khoảng trắng
split(str[num]) # mặc định là cắt theo khoảng trắng. 

3. Datetimes:

+ Làm việc với time:
import time
import datetime

time.time() # trả về thời gian hiện tại của hệ thống dạng số
time.localtime(time.time()) #trả về thời gian hiện tại của hệ thống dạng các thành phần của datetime
time.asctime(time.localtime(time.time())) # trả về chuỗi thời gian theo định dạng

from datetime import datetime
print(datetime.now())

datetime(year, month, day) # nếu ngày tháng ko hợp lệ sẽ phát sinh lỗi
print(datetime(2017, 10, 10))

date_var.strftime(%d - %m - %y) # hiển thị ngày của chuỗi theo định dạng mẫu
date2 = datetime(2017, 2, 18)
print("Ngày tháng năm: ", date2.strftime(%d - %m - %Y)) # %Y, hiển thị năm đủ 4 số, %b: tháng kiểu chữ

+ Làm việc với calendar:
import calendar

calendar.isleap(year) # trả về true, false

calendar.monthcalendar(year, month): trả về danh sách các ngày trong tháng, năm được chọn, chia theo từng tuần, với giá trị 0 là ngày ko nằm trong tháng của năm.

calendar.weekday(year, month, day) # trả về thứ của ngày/tháng/năm (0: Monday, 1: Tuesday...)

calendar.monthrange(year,month) # trả về 2 phần tử: ngày đầu tiên trong tháng và số ngày trong tháng











Bài tập:
1. Bài 6_1_tim_min_max_2.py
2. Bài 6_2_tim_gttd_x_2.py
3. Bài 6_3_tinh_S_2.py
4. Bài 6_4_tinh_A_2.py
5. Bài 6_5_giai_PT_bac_2.py
6. Bai 6_6_xu_ly_chuoi.py
7. Bai 6_7_xu_ly_thoi_gian.py
