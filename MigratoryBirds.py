#ProblemStatement:
#https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

from collections import Counter

def migratoryBirds(arr):
    bird_counts = Counter(arr)
    max_count = max(bird_counts.values())
    most_frequent_birds = [bird_id for bird_id, count in bird_counts.items() if count == max_count]
    return min(most_frequent_birds)

#Logic:
# To find the most frequently sighted bird species from a list. Using a Counter, we tally the occurrences of each bird. Then find the maximum count among the bird species. If there are multiple birds with the highest count, we select the one with the lowest ID, which is the most frequent. This approach finds and returns the ID of the most commonly spotted bird.