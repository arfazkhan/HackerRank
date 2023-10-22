#ProblemStatement:
#https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true

def viralAdvertising(n):
    shared = 5  
    cumulative_likes = 0

    for day in range(1, n + 1):
        liked = shared // 2  
        cumulative_likes += liked
        shared = liked * 3  

    return cumulative_likes

#Logic:
#