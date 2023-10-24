import math

def encryption(s):
    s = s.replace(" ", "")  
    L = len(s)
    rows = int(math.sqrt(L))
    columns = rows if rows * rows >= L else rows + 1
    
    result = ""
    
    for c in range(columns):
        result += s[c::columns] + " "

    return result

