#https://www.hackerrank.com/challenges/bigger-is-greater/problem

def biggerIsGreater(w):
    
    w = list(w)
    
    #
    i = len(w) - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1
    
    if i == -1:
        return "no answer"  
    
    
    j = len(w) - 1
    while w[j] <= w[i]:
        j -= 1
    
    
    w[i], w[j] = w[j], w[i]
    
    
    w[i + 1:] = reversed(w[i + 1:])
    
    return ''.join(w)

#Logic:
#I start by converting the string ‘w’ into a list of characters. Then, I iterate from the end of the list to the beginning, looking for the first character that is lexicographically smaller than its next character. If I don’t find such a character, it means that ‘w’ is the last permutation and I return “no answer”. If I do find such a character, I then iterate from the end of the list to this character, looking for the smallest character that is greater than it. I swap these two characters and then reverse the part of the list that comes after the first swapped character. Finally, I join the list back into a string and return it. This gives me the next lexicographically greater permutation of ‘w’.