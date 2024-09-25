done = False
for num in range(1,1000001):
    tempList = [num]
    if num % 10000 == 0:
        print(num)
    # print(num)
    while True:
        sumfactorial = 0
        temp = list(str(tempList[-1]))
        for term in temp:
            factorial = 1
            for x in range(1,int(term)+1):
                factorial *= x
            sumfactorial += factorial
        
        if sumfactorial not in tempList:
            tempList.append(sumfactorial)
        else:
            break
        
        if len(tempList) > 63:
            if tempList[60] == temp[0]:
                print(num)
                done = True
                
            break
    
    if done == True:
        break

