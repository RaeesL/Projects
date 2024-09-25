# gamma = ""
# epsilon = ""
# with open ("./adventOfCode/dayThree.txt", "r") as binaryText:
#     values = binaryText.readlines()
#     for x in range(12):
#         majority = {"0":0, 
#                     "1":0}
#         for line in values:
#             majority[line[x]] += 1
        
#         print(majority)
#         if majority["1"] > majority["0"]:
#             gamma += "1"
#         else:
#             gamma += "0"

#     print(gamma)

#     for char in gamma:
#         if char == "0":
#             epsilon += "1"
#         else:
#             epsilon += "01"
    
#     print(epsilon)


values = []

with open ("./adventOfCode/dayThree.txt", "r") as binaryText:
    for line in binaryText:
        values.append(line.rstrip())

for index in range(len(values[0])):
    majority = {"0":0, 
                "1":0}
    for term in values:
        majority[term[index]] += 1

    if majority["1"] < majority["0"]:
        for term in range(len(values)-1,-1,-1):
            if values[term][index] == "0":
                values.remove(values[term])
                

    else:
        for term in range(len(values)-1,-1,-1):
            if values[term][index] == "1":
                values.remove(values[term])

    print("\n",index, majority)
    print("")
    print(values)
    print(len(values))
    

