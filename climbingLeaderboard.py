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

#Logic:
#First, I clean up the ranked list by removing duplicate scores, ensuring a simplified and efficient ranking. Then, I start at the end of the leaderboard and, for each of the player's scores, I work backward to find their rank by comparing their score with the scores on the leaderboard. The result is a list of the player's ranks for each score. It's like guiding the player through the leaderboard to determine their position as they compete.