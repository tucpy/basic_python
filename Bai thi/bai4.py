
tu_dien = { "man": ["dan ong"], "woman": ["dan ba", "phu nu"], "house": ["nha", "ngoi nha","can nha"],
"sun": ["mat troi"], "moon": ["mat trang"], "earth": ["trai dat", "qua dat", "dia cau"],
"mountain": ["nui", "ngon nui"]}

from random import randint

tiep_tuc = True
while tiep_tuc:
    cac_key = list(tu_dien.keys())
    #print(cac_key)
    i = randint(0, len(tu_dien) - 1)
    lay_key = cac_key[i]
    #print(lay_key)
    lay_value = tu_dien[lay_key]
    #print(lay_value)
    print("Ban hay cho biet '%s' co nghia gi?" %(lay_key))
    tra_loi = str(input())
    for i in lay_value:
        if tra_loi == i:
            dung = True
            break
        else:
            dung = False
            
    if dung == True:
        print ("Ban da doan dung")
    else:
        print ("Ban da doan sai. Nghia cua tu '%s' phai la:"%(lay_key))
        for i in lay_value:
            print("- %s" %i)
    

    tt = input("\nBan co muon tiep tuc khong (y/n)?")
    if tt == "y" or tt == "Y":
        tiep_tuc = True
    else:
        tiep_tuc = False