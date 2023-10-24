#ProblemStatement:
#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true

def climbingLeaderboard(ranked, player):
    result = []
    ranked = list(dict.fromkeys(ranked))  

    rank_index = len(ranked) - 1  

    for score in player:
        while rank_index >= 0 and score >= ranked[rank_index]:
            rank_index -= 1 
        result.append(rank_index + 2)  
    return result
