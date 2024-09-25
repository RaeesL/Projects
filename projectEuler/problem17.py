words = {1:"one",
         2:"two",
         3:"three",
         4:"four",
         5:"five",
         6:"six",
         7:"seven",
         8:"eight",
         9:"nine",
         10:"ten",
         11:"eleven",
         12:"twelve",
         13:"thirteen",
         14:"fourteen",
         15:"fifteen",
         16:"sixteen",
         17:"seventeen",
         18:"eighteen",
         19:"nineteen",
         20:"twenty",
         30:"thirty",
         40:"forty",
         50:"fifty",
         60:"sixty",
         70:"seventy",
         80:"eighty",
         90:"ninety",
         100:"hundred",
         "and":"and",
         0:""
         }

total = ""
for x in range(1000):
    if x//100 >= 1:
        total += words[x//100] + words[100]
        if x%100 > 0:
            total += words["and"]
    if x%100//10 == 1:
        total += words[x%100]
    elif x//10 > 1 or x//10 == 0:
        total += words[x%100 - x%10] + words[x%10]
    

print(total+"onethousand")