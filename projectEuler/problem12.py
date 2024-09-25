found = False
total = 0
count = 0
while found == False:
    count += 1
    total += count
    factors = 0
    for x in range(1,int(round(total**0.5))):
        if total % x == 0:
            factors += 2
    
    if factors > 500:
        found = True
        break

print(total)