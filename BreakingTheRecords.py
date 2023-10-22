#ProblemStatement:
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

def breakingRecords(scores):
    max_score = scores[0]
    min_score = scores[0]

    max_count = 0
    min_count = 0
    
    for score in scores:
        if score > max_score:
            max_score = score
            max_count += 1
        elif score < min_score:
            min_score = score
            min_count += 1
   
    return [max_count, min_count]

#Logic:
#It takes a list of my scores and keeps tabs on how many times I break my own records. At the start, it sets my first score as both my best and worst. Then, as I play, if I get a higher score, it's like, "Whoa, new high score!" and that count goes up. And if I get a lower score, it's like, "Oops, new low score!" and the other count goes up. When I'm done, it tells me how many times I aced it and how many times I slipped up.