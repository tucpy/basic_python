'''
check how many "0" a number end with
'''

n = int(input("n: "))

factorial = 1
for i in range(1,n+1):
    factorial *= i

print("factorial: ", factorial)

count = 0
while (factorial > 0):
    digit = factorial % 10
    if  digit != 0:
        break
    else:
        count += 1
    factorial /= 10

print("out: ", count) 
    
