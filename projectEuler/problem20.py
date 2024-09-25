total = 1
for x in range(1,101):
    total *= x

digitTotal = 0
for char in str(total):
    digitTotal += int(char)
    
print(total, "\n", digitTotal)