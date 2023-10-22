#ProblemStatement:
#https://www.hackerrank.com/challenges/taum-and-bday/problem?isFullScreen=true
def taumBday(b, w, bc, wc, z):
    if bc > wc + z:
            return b * (wc + z) + w * wc
    elif wc > bc + z:
            return b * bc + w * (bc + z)
    else:   
        return b * bc + w * wc

#Logic:
#This function takes the input for  the number of black gifts (b), the number of white gifts (w), the cost of a black gift (bc), the cost of a white gift (wc), and the cost to convert one color gift to the other color (z). It calculates and returns the minimum cost to purchase the gifts for a birthday celebration. The function determines whether it's more cost-effective to buy gifts of one color and convert some to the other color or to simply buy gifts as is, depending on the given costs and conversion expense (z). The goal is to minimize the overall cost while meeting the gift requirements for the celebration.