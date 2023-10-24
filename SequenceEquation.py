def permutationEquation(p):
    result = []
    
    pos_dict = {}
    for i, x in enumerate(p, start=1):
        pos_dict[x] = i
    
    for x in range(1, len(p) + 1):
        second_permutation = pos_dict[pos_dict[x]]
        result.append(second_permutation)