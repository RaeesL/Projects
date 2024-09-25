valid = True
final = []
for x in range(999,99,-1):
    for y in range(999,99,-1):
        subtotal = x*y
        lst = list(str(subtotal))
        for z in range(len(lst)//2):
            if lst[z] != lst[len(lst)-z-1]:
                valid = False
                break
            else:
                valid = True
        if valid == True:
            final.append(x*y)
    if valid == True:
        break

print(sorted(final))