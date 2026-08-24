produto = 1
for num in range(92, 1479):
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
    if primo:
        produto = produto * num
print(produto)