#https://www.hackerrank.com/challenges/fair-rations/problem?isFullScreen=true
def fairRations(B):
    odd = [i for i, b in enumerate(B) if b % 2 == 1]

    if len(odd) % 2 == 1:
        return "NO"

    loaves = sum(odd[i + 1] - odd[i] for i in range(0, len(odd), 2))
    
    return str(loaves * 2)  

#Logic:
#First, I find all the number of people needing an extra loaf (those with odd bread counts). If the count of such people is odd, it's impossible to distribute fairly, so I return "NO." If there's an even count of needy people, I calculate the additional loaves required by looking at the gaps between their number. These gaps represent the number of extra loaves needed for each pair of adjacent needy people. Multiplying this count by 2 ensures a fair distribution. This approach guarantees fairness and provides the required additional loaves efficiently.