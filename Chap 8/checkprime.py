from my_module import checkprime
lst = range(2,8)
prime = []

for item in lst:
    if checkprime(item):
        prime.append(item)
print(prime)