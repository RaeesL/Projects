count = 1
start = 0
for x in range(1, 1000001):
    tempcount = 1
    num = x
    if x % 10000 == 0:
        print(x)
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3 + 1
        tempcount += 1
    if tempcount > count:
        count = tempcount
        start = x
        
print(start, count)
