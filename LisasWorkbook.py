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

