primelist = []
with open("primes.txt", "r") as file:
    try:
        for line in range(3001135):
            templine = file.readline().rstrip()
            primelist.append(int(templine))
    except:
        print(templine)
    
print(primelist[-1])
count = 0
for num1 in primelist:
    for num2 in range(len(primelist)-1, 0, -1):
        if num1*primelist[num2] < 100000000:
            count += num2 + 1
            break

        
print(count/2 + 1229/2)
