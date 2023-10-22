#ProblemStateent:
#https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true

def equalizeArray(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    max_count = max(count_dict.values())
    deletions = len(arr) - max_count
    return deletions

#Logic:
# In this code, I'm finding the minimum number of deletions needed to make all elements in an array equal. First, I create a dictionary to count the occurrences of each element, and then identify the most frequently occurring element. The deletions required will be the total number of elements minus the count of the most frequent element. This approach efficiently helps me determine the minimal deletions to equalize the array. It's like figuring out how many elements I need to remove to have them all the same