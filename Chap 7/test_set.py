'''
set_string = {"Kim", "Mộc", "Thủy", "Hỏa", "Thổ"}
print(set_string)
'''

'''
str1 = "Hello"
print(type(set_string))
'''

'''
item = set_string.pop()
print(item)
print(set_string)
'''



setA = {1,2,3}
setB = {1,4,5}

setC = setA ^ setB 
print(setC)



toan_tu_and = setA & setB
toan_tu_or = setA | setB
toan_tu_xor = toan_tu_or - toan_tu_and


print(toan_tu_and)
print(toan_tu_or)
print(toan_tu_xor)
