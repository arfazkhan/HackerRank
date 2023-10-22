import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
    lcm_a = a[0]
    for num in a[1:]:
        lcm_a = lcm(lcm_a, num)

    gcd_b = b[0]
    for num in b[1:]:
        gcd_b = gcd(gcd_b, num)

    count = 0
    x = lcm_a
    while x <= gcd_b:
        if gcd_b % x == 0:
            count += 1
        x += lcm_a

    return count

#Logic:
#First, I figure out the common factors in two sets of numbers using the GCD and LCM. Then, I go on a hunt for special numbers that fit between these sets, can be divided by both, and count how many of them there are.