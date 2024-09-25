count = 0
for x in range(10012233445566778899, 99887766554433221100, 11):
    dictionary = {str(x):0 for x in range(10)}
    for y in str(x):
        dictionary[str(y)] += 1
    if dictionary == {str(x):2 for x in range(10)}:
        count += 1
        if count % 100 == 0:
            print(count, x)
            
print(count)
    
