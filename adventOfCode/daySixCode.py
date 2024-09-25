
with open("daySix.txt", "r") as file:
    text = file.readlines()[0].split(",")
    
    
for term in range(len(text)):
    text[term] = int(text[term])
    

dictionary = {x:0 for x in range(9)}
for term in text:
    dictionary[term] += 1

for count in range(256):
    temp8 = dictionary[8]
    temp7 = dictionary[7]
    temp6 = dictionary[6]
    temp5 = dictionary[5]
    temp4 = dictionary[4]
    temp3 = dictionary[3]
    temp2 = dictionary[2]
    temp1 = dictionary[1]
    temp0 = dictionary[0]
    dictionary[8] = temp0
    dictionary[7] = temp8
    dictionary[6] = temp7 + temp0
    dictionary[5] = temp6
    dictionary[4] = temp5
    dictionary[3] = temp4
    dictionary[2] = temp3
    dictionary[1] = temp2
    dictionary[0] = temp1
    
    
# for count in range(256):
#     print(count)
#     for term in range(len(text)):
#         if text[term] == 0:
#             text.append(8)
#             text[term] = 6
#         else:
#             text[term] -= 1

         
print(sum(dictionary.values()))