#https://www.hackerrank.com/challenges/lisa-workbook/problem?isFullScreen=true
def workbook(n, k, arr):
    special_problems = 0
    page = 1

    for problems in arr:
        for problem in range(1, problems + 1):
            if problem == page:
                special_problems += 1

            if problem % k == 0 or problem == problems:
                page += 1

    return special_problems

#Logic:
#We begin with a count of special_problems set to 0 and initialize the page number to 1. For each chapter's problems in the arr, we iterate through the problems using a loop. We check if the problem number matches the current page number, and if so, we increment the special_problems count. Additionally, we keep track of the page number, ensuring it advances when we reach either the end of a chapter or after k problems, making it easy to count special problems per page. Finally, we return the total count of special problems found.