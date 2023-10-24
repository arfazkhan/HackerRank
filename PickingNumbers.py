def pickingNumbers(a):
    count_dict = {}
    max_length = 0

    for num in a:
        count_dict[num] = count_dict.get(num, 0) + 1

    for num in count_dict:
        max_length = max(max_length, count_dict[num] + count_dict.get(num + 1, 0))

    return max_length