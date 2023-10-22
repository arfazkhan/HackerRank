#ProblemStatement:
#https://www.hackerrank.com/challenges/acm-icpc-team/problem?isFullScreen=true

def acmTeam(topic):
    n = len(topic)
    m = len(topic[0])
    
    max_topics = 0
    team_count = 0
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            topics_known = sum(1 for x, y in zip(topic[i], topic[j]) if x == '1' or y == '1')
            if topics_known > max_topics:
                max_topics = topics_known
                team_count = 1
            elif topics_known == max_topics:
                team_count += 1
    
    return [max_topics, team_count]

#logic:
#We go through all possible pairs of teams and calculate how many topics they collectively know. We keep track of the maximum topics known and how many teams share that knowledge. It's like discovering the most knowledgeable teams and counting how many of them are at the top. 