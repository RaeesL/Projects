pentagonal = [(3*x**2 - x)/2 for x in range(1,1000000)]

found = False
for term in pentagonal:
    for term2 in pentagonal:
        if term2 != term:
            if term + term2 in pentagonal:
                if (term - term2 in pentagonal or term2 - term in pentagonal):
                    found = True
                    break
    if found == True:
        break
    
print(term2, term)

