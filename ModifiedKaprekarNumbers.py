#https://www.hackerrank.com/challenges/kaprekar-numbers/problem?isFullScreen=true

def kaprekarNumbers(p, q):
    kaprekar_nums = []

    for num in range(p, q + 1):
        square = num * num
        num_str = str(num)
        square_str = str(square)

        d = len(num_str)
        r = int(square_str[-d:]) 
        l = int(square_str[:-d]) if square_str[:-d] else 0  

        if r + l == num:
            kaprekar_nums.append(num)

    if kaprekar_nums:
        print(" ".join(map(str, kaprekar_nums)))
    else:
        print("INVALID RANGE")

