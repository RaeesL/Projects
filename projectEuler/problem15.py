#how many different ways can you add 1 to two variables up to 20

n1 = 1
r1 = 1
for x in range(1,41):
    n1 *= x
    
for y in range(1,21):
    r1 *= y
    

print(n1/r1/r1)