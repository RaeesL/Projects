try:
    index = 2
    triangle = []
    pentagonal = []
    hexagonal = []
    while True:
        newT = index*(index+1)/2
        newP = index*(3*index - 1)/2
        newH = index*(2*index - 1)
        triangle.append(int(newT))
        pentagonal.append(int(newP))
        hexagonal.append(int(newH))
        
        if newT in pentagonal and newT in hexagonal and newT != 40755:
            print(triangle[-1])
            break
        elif newP in triangle and newP in hexagonal and newP != 40755:
            print(pentagonal[-1])
            break
        elif newH in triangle and newH in triangle and newH != 40755:
            print(hexagonal[-1])
            break
        
        index += 1
        

except:
    print(index)