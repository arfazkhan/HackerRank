#ProblemStatement:
#https://www.hackerrank.com/challenges/cut-the-sticks/

def cutTheSticks(arr):
    result = [] 

    while arr:
        result.append(len(arr))
        min_length = min(arr)
        arr = [stick - min_length for stick in arr if stick - min_length > 0]

    return result

#Logic:
#I'm simplifying a collection of sticks by repeatedly cutting the longest ones until there are none left. I start with a list of all the stick lengths and initialize an empty result list. As long as there are sticks left, I count them, add the count to the result, find the length of the shortest stick, and update the list with the remaining sticks after cutting the minimum length from each. The result is a list of how many sticks are cut at each step, effectively reducing the sticks to the smallest size. It's like a step-by-step process to minimize the sticks.