from math import factorial as f

count = 0
for n in range(23,101):
    for r in range(2,n):
        nr = f(n)/(f(r)*f(n-r))
        if nr > 1000000:
            count += 1

print(count)