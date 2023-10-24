#ProblemStatement:
#https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

from collections import Counter

def migratoryBirds(arr):
    bird_counts = Counter(arr)
    max_count = max(bird_counts.values())
    most_frequent_birds = [bird_id for bird_id, count in bird_counts.items() if count == max_count]
    return min(most_frequent_birds)
