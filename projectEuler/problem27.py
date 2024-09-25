with open("primes.txt", "r") as file:
    primes = file.readlines()
    
for term in range(len(primes)):
    primes[term] = int(primes[term].rstrip())
  
big = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1001):
        count = 0
        print(x, y)
        while (count**2 + x*count + y) in primes:
            print(count**2 + x*count + y)
            count += 1
        if count > big:
            record = [x,y]
            big = count

print(big, record)