import csv


# f = open("sinh_vien.csv", encoding="utf-8")
# data = []
# for row in csv.reader(f):
#     print("Họ tên:", row[0], "- Tuổi:", row[1])
#     row[0] = row[0].upper()
#     data.append(row)
# f.close()
# print(data)


f = open("sample.csv")
lst = []
for row in csv.reader(f):
    a = row[3].split()
    lst += a
f.close()
# print(lst)


# Đếm số lần xuất hiện và ghi ra tập tin sample2.csv
list_full = []
for item in lst:
    b = (item + " " + str(lst.count(item))).split()
    list_full.append(b)
    print(list_full)
    # f = open("sample2.csv", "w", encoding="utf-8", newline="")
    # writer = csv.writer(f).writerows(list_full)





    







# # Define Data
# RESULTS = ['apple','cherry','orange','pineapple','strawberry']

# # Open File
# resultFyle = open("sample2.csv",'w')

# # Write data to file
# for r in RESULTS:
#     resultFyle.write(r + "\n")
# resultFyle.close()