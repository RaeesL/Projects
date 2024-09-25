done = False
for x in range(998,0,-1):
    for y in range(998, 0, -1):
        z = (x**2+y**2)**0.5
        if x + y + z == 1000:
            done = True
            break
    if done == True:
        break

print(x*y*z)