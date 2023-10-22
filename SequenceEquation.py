#ProblemStatement:
#https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true

def permutationEquation(p):
    result = []
    
    pos_dict = {}
    for i, x in enumerate(p, start=1):
        pos_dict[x] = i
    
    for x in range(1, len(p) + 1):
        second_permutation = pos_dict[pos_dict[x]]
        result.append(second_permutation)

#logic:
#In this function, I'm calculating the second permutation of a given sequence p. First, I create a dictionary, pos_dict, where the keys are the elements of p and the values are their corresponding positions in the sequence. Then, I iterate through the range from 1 to the length of p, finding the second permutation by using pos_dict twice. For each x, I find its position in pos_dict, and then find the position of that result again in pos_dict. This computes the second permutation and stores the results in the list "result". It's a systematic way to find the desired permutation of the given sequence p.