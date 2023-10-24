def serviceLane(n, cases, width):
    results = []
    for case in cases:
        entry, exit = case[0], case[1]
        min_width = min(width[entry:exit + 1])
        results.append(min_width)
    return results