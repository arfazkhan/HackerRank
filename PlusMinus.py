def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    
    total_elements = len(arr)
    print("{:.6f}".format(positive_count / total_elements))
    print("{:.6f}".format(negative_count / total_elements))
    print("{:.6f}".format(zero_count / total_elements))