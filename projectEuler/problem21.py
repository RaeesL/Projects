thousand = [x for x in range(1,10000)]
try:
    lst = []
    index = -1
    amicable = 0
    while True: 
        factors = 0
        factorFactors = 0
        # print(thousand[index])
        for x in range(1,thousand[index]):
            if thousand[index] % x == 0:
                factors += x
            
        for x in range(1,factors):
            if factors % x == 0:
                factorFactors += x 
            
        if thousand[index] == factorFactors:
            if thousand[index] not in lst:                
                amicable += thousand[index] + factors
                print(thousand[index], factors)
                lst.append(thousand[index])
                lst.append(factors)
        
        index -= 1
            
except:
    print(amicable)
