
finalList = []
for a in range(10):
    string = ""
    string += str(a)
    
    for b in range(10):
        if str(b) not in string:
            string += str(b)
            
            for c in range(10):
                if str(c) not in string:
                    string += str(c)
                    
                    for d in range(10):
                        if str(d) not in string:
                            string += str(d)
                            
                            for e in range(10):
                                if str(e) not in string:
                                    string += str(e)
                                    
                                    for f in range(10):
                                        if str(f) not in string:
                                            string += str(f)
                                            
                                            for g in range(10):
                                                if str(g) not in string:
                                                    string += str(g)
                                                    
                                                    for h in range(10):
                                                        if str(h) not in string:
                                                            string += str(h)
                                                            
                                                            for i in range(10):
                                                                if str(i) not in string:
                                                                    string += str(i)
                                                                    
                                                                    for j in range(10):
                                                                        if str(j) not in string:
                                                                            string += str(j)
                                                                            finalList.append(string)
                                                                    
                                                                    
                                                                        string = string[:9]
                                                                    string = string[:8]
                                                            string = string[:7]
                                                    string = string[:6]
                                            string = string[:5]
                                    string = string[:4]
                            string = string[:3]
                    string = string[:2]
            string = string[:1]
    string = string[:0]
    if len(finalList) > 1000000:
        break
        
                
print(finalList[999999])