with open ("dayFour.txt", "r") as file:
    matrices = file.readlines()

with open ("dayFour2.txt", "r") as file:
    numbers = file.readlines()

while "\n" in matrices:
    matrices.remove("\n")

numbers = numbers[0].split(",")

for index in range(len(matrices)):
    matrices[index] = matrices[index].rstrip().lstrip()
    matrices[index] = matrices[index].split()

matrices.remove([])

finalList = []
for x in range(0,len(matrices),5):
    tempList = []
    for y in range(5):
        tempList.append(matrices[x+y])
    finalList.append(tempList)


def checker(numbers, finalList):
    done = {y:False for y in range(100)}
    checked = []
    for number in numbers:
        for matrix in range(len(finalList)):
            for iteColumn in range(len(finalList[matrix])):
                for iteRow in range(len(finalList[matrix][iteColumn])):
                    if finalList[matrix][iteColumn][iteRow] == number:
                        checked.append([matrix,iteRow,iteColumn])
    
            column = {x:0 for x in range(5)}
            row = {x:0 for x in range(5)}
            for term in checked:
                if term[0] == matrix:
                    row[term[1]] += 1
                    column[term[2]] += 1
                    if 5 in row.values() or 5 in column.values():
                        print(matrix)
                        done[matrix] = True
                        print(done)
                        if all(done.values()) == True:    
                            return checked, matrix, number
            

            


# print(numbers, finalList)                
checked, matrix, number = checker(numbers, finalList)
print(matrix)

total = 0
print(finalList[matrix])
for row in finalList[matrix]:
    for column in row:
        print(int(column))
        total += int(column)
print(total)
for term in checked:
    if term[0] == matrix:
        print(term, finalList[matrix][term[2]][term[1]])
        total -= int(finalList[matrix][term[2]][term[1]])
print(number)
total *= int(number)
print(total)

# print(matrix)
# print(finalList[27][0][1])


