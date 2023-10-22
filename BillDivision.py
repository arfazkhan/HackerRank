#ProblemStatement:
#https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true

def bonAppetit(bill, k, b):
    total_cost = sum(bill) - bill[k]

    anna_share = total_cost // 2

    if b == anna_share:
        print("Bon Appetit")
    else:
        print(b - anna_share)

#Logic:
#In this function, I'm handling a restaurant bill situation with my friend Anna. We're splitting the bill but excluding the cost of the item she didn't eat, whiich is denoted by index "k." First, I calculate the total cost by summing up all the items except the excluded one. Then, I find Anna's share by dividing the total cost by 2. If her share matches the amount she paid, we print "Bon Appetit." If not, we print the difference between what she paid and her actual share.