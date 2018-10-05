# Đọc file
f = open("1.2_bai_tho_co_dau.txt", "r", encoding="utf-8")
noi_dung = f.read()
print(noi_dung)
f.close()

# Ghi tiếp theo
f = open("1.2_bai_tho_co_dau.txt", "a+", encoding="utf-8")
noi_dung = "\n\nBước tới đèo ngang bóng xế tà"
noi_dung += "\nCỏ cây chen lá đá chen hoa"
noi_dung += "\nLom khom dưới núi tiều vài chú"
noi_dung += "\nLác đác bên sông chợ mấy nhà"
f.write(noi_dung)
f.close()
