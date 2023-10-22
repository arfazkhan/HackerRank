#ProblemStatement:
#https://www.hackerrank.com/challenges/library-fine

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 <= d2):
        return 0
    elif y1 == y2 and m1 == m2:
        return 15 * (d1 - d2)
    elif y1 == y2 and m1 > m2:
        return 500 * (m1 - m2)
    else:
        return 10000

#Logic:
#I'm calculating the fine for a library book return. I compare the return date (d1, m1, y1) with the due date (d2, m2, y2). If the return is on or before the due date, there's no fine (return 0). If the return is within the same month, I calculate the fine based on the number of days late. If the return is in a later month of the same year, I calculate the fine based on the number of months late. If the return is in a later year, there's a fine of 10000.