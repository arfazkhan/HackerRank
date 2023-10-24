def fairRations(B):
    odd = [i for i, b in enumerate(B) if b % 2 == 1]

    if len(odd) % 2 == 1:
        return "NO"

    loaves = sum(odd[i + 1] - odd[i] for i in range(0, len(odd), 2))
    
    return str(loaves * 2)  

