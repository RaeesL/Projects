lst= []
with open("primes.txt", "r") as file:
    for line in range(148935):
        lst.append(file.readline(line).rstrip())

total = 0
print(lst[:5])
for term in lst:
    if term != "":
        total += int(term)

print(total)