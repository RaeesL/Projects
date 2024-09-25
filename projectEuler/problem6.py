total, sqtotal = 0, 0
for x in range(101):
    total += x
    sqtotal += x**2

total = total**2

print(sqtotal-total)