# -*- coding: utf-8 -*-
import csv

f = open("sinh_vien_edit.csv", encoding="utf-8")
data = []
for row in csv.reader(f):
    # Kiểu list
    # print(row)

    # Tường minh => Không phải kiểu list
    # print("Họ tên:", row[0], "- Tuổi:", row[1])

    # Xử lý
    row[0] = row[0].upper()
    data.append(row)
print(data)
f.close()


# Ghi data ra tập tin sinh_vien_upper.csv
f = open("sinh_vien_upper.csv", "w", encoding="utf-8", newline="")
for item in data:
    csv.writer(f).writerow(item)
f.close()

