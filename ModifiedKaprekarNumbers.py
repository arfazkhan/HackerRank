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

#Logic:
#I start by creating an empty list to store the Kaprekar numbers. Then, I iterate over each number in the range from ‘p’ to ‘q’ inclusive. For each number, I square it and convert both the number and its square into strings. I then split the string representation of the square into two parts: a right part consisting of the last ‘d’ digits (where ‘d’ is the number of digits in the original number) and a left part consisting of the remaining digits. If there are no remaining digits, I consider the left part to be zero. I then check if the sum of the right and left parts equals the original number. If it does, I append the number to my list of Kaprekar numbers. After checking all numbers in the range, if I have found any Kaprekar numbers, I print them out. Otherwise, I print “INVALID RANGE”.