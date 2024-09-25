with open("problem22txt.txt", "r") as file:
    names = file.read()
    names = names.split(",")
    
# print(names)
for term in range(len(names)):
    names[term] = names[term].replace("\"", "")

# print(names)
names = sorted(names)
print(names)


total = 0
for term in range(len(names)):
    subtotal = 0
    for character in names[term]:
        subtotal += ord(character) - 64
    total += (subtotal * (term+1))
    
print(total)
