#ProoblemStatement:
#https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

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

#Logic:
# I want to understand the proportions of positive, negative, and zero values. So, I'm counting how many numbers fall into each of these categories. Then, I calculate and print the fractions of positive, negative, and zero values relative to the total number of elements