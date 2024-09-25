numbers = []
with open("problemthirteentext.txt", "r") as file:
    for line in file:
        numbers.append(line.rstrip())

total = 0
for term in range(len(numbers)):
    total += int(numbers[term])
    
    
print(total)