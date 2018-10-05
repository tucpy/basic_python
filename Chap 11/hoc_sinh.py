# Nhập Họ tên, điểm Toán, Lý, Hóa của 5 học sinh
# "Lê Văn Bảo",10,8.5,9.0
# ...
# Tính điểm trung bình = (Toán + Lý + Hóa) / 3    =>    lấy 1 số lẻ, làm tròn
# Ghi vào tập tin ket_qua.csv
# Lê Văn Bảo,10,8.5,9.0,9.2

import csv
dtb = 0
data = []
f = open("hoc_sinh.csv", encoding="utf-8")
for row in csv.reader(f):
    dtb = (float(row[1]) + float(row[2]) + float(row[3])) / 3
    print("Họ tên:", row[0], "- Toán:", row[1], "- Lý:", row[2], "- Hóa:", row[3], "- ĐTB:", round(dtb,1))
    row.append(round(dtb, 1))
    data.append(row)
f.close()
print(data)


# Ghi data ra tập tin ket_qua.csv
f = open("ket_qua.csv", "w", encoding="utf-8", newline="")
for item in data:
    csv.writer(f).writerow(item)
f.close()