
#https://www.hackerrank.com/challenges/encryption
import math

def encryption(s):
    s = s.replace(" ", "")  
    L = len(s)
    rows = int(math.sqrt(L))
    columns = rows if rows * rows >= L else rows + 1
    
    result = ""
    
    for c in range(columns):
        result += s[c::columns] + " "

    return result

#Logic:
#we're encrypting a message by arranging its characters into a grid and then reading the characters column by column. We remove spaces from the message and calculate the grid's dimensions based on the square root of the message length, visualizing it as a rectangular layout. We then construct the encrypted message by iterating through the columns, collecting characters from the original message and separating words with spaces. This method efficiently transforms the message into an encrypted format for secure communication.