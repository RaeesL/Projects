with open("primes.txt","r") as lst:
    primes = lst.readlines()
    
for x in range(len(primes)):
    primes[x] = int(primes[x].rstrip())

end = int(input("Enter the number you wish to find primes until: "))
count = 0
if end > primes[-1]:
    for x in range(primes[-1]+2, end+1,2):
        valid = True
        sqrt = x**0.5
        for y in range(len(primes)):
            if y < sqrt:
                if x % primes[y] == 0:
                    valid = False
                    break
            else:
                break
        if valid == True:
            count += 1
            if count == 10000:
                count = 0
                print("10000 Primes Found!", x)
            primes.append(x)
    
        
with open("primes.txt","w") as lst:
    for term in primes:
        lst.write(str(term)+"\n")
