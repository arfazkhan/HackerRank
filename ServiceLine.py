#https://www.hackerrank.com/challenges/service-lane/problem?isFullScreen=true
def serviceLane(n, cases, width):
    results = []
    for case in cases:
        entry, exit = case[0], case[1]
        min_width = min(width[entry:exit + 1])
        results.append(min_width)
    return results

#Logic:
# In this function, we're given a list of cases, where each case signifies a specific segment within the width list. To find the minimum width in each segment, I loop through the cases. For every case, I extract the start and end indices, then use Python's min function to find the smallest width within that segment of the width list. These minimum widths are collected in a results list. After processing all cases, I return this list containing the minimum widths for each specified segment. it efficiently calculates and provides the minimum widths for various segments, making it straightforward and practical. 

#Note:
# fix the predefined argument with "result = serviceLane(n, cases, width)" instead of "result = serviceLane(n, cases)" or else you get runtime error.
