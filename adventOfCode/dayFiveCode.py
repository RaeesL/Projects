with open("dayFive.txt", "r") as file:
    text = file.readlines()

newList = []
for term in text:
    newList.append([term[:7].rstrip(), term[10:].lstrip().rstrip()])


for term in range(len(text)):
    for coords in range(2):
        newList[term][coords] = newList[term][coords].split(",")


dictionary = {}

for line in newList:
    
    for coords in range(2):
        for coord in range(2):
            line[coords][coord] = int(line[coords][coord])
            
    if line[0][0] == line[1][0]:
        for x in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1])+1):
            if str([line[0][0], x]) not in dictionary:
                dictionary[str([line[0][0], x])] = 1
            else:
                dictionary[str([line[0][0], x])] += 1
                            
    if line[0][1] == line[1][1]:
        for y in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1):
            if str([y, line[0][1]]) not in dictionary:
                dictionary[str([y, line[0][1]])] = 1
            else:
                dictionary[str([y, int(line[0][1])])] += 1


    if (max(line[0][0], line[1][0]) - min(line[0][0], line[1][0])) == (max(line[0][1], line[1][1]) - min(line[0][1], line[1][1])):
        print(line)
        if line[0][0] < line[1][0]:
            if line[0][1] < line[1][1]:
                print("branch 1")
                for diag in range(line[1][0] - line[0][0]+1):
                    if str([line[0][0] + diag, line[0][1] + diag]) not in dictionary:
                        dictionary[str([line[0][0] + diag, line[0][1] + diag])] = 1
                    else:
                        dictionary[str([line[0][0] + diag, line[0][1] + diag])] += 1
            
            else:
                print("branch 2")
                for diag in range(line[1][0] - line[0][0]+1):
                    if str([line[0][0] + diag, line[0][1] - diag]) not in dictionary:
                        dictionary[str([line[0][0] + diag, line[0][1] - diag])] = 1
                    else:
                        dictionary[str([line[0][0] + diag, line[0][1] - diag])] += 1
        
        else:
            if line[0][1] < line[1][1]:
                print("branch 3")
                for diag in range(line[0][0] - line[1][0]+1):
                    if str([line[0][0] - diag, int(line[0][1]) + diag]) not in dictionary:
                        dictionary[str([line[0][0] - diag, line[0][1] + diag])] = 1
                    else:
                        dictionary[str([line[0][0] - diag, line[0][1] + diag])] += 1
            
            else:
                print("branch 4")
                for diag in range(line[0][0] - line[1][0]+1):
                    if str([line[0][0] - diag, line[0][1] - diag]) not in dictionary:
                        dictionary[str([line[0][0] - diag, line[0][1] - diag])] = 1
                    else:
                        dictionary[str([line[0][0] - diag, line[0][1] - diag])] += 1
            

                
count = 0
for coord in dictionary:
    if dictionary[coord] >= 2:
        count += 1

# print(dictionary)
# print(newList)
print(count)
