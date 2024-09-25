with open ("primes.txt", "r") as file:
    primelist = file.readlines()
    
for term in range(len(primelist)):
    primelist[term] = int(primelist[term].rstrip())

remainder = 0
index = 7037
while remainder < 10000000000:
    index += 1
    if index != 21033: #broken for some reason
        num = primelist[index]
        temp = ((num-1)**index) + ((num+1)**index)
        remainder = temp % (num**2)




print(index)
print(remainder)