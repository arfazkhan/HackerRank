#ProblemStatement:
#https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true
def organizingContainers(container):
    n = len(container)
    container_sums = [sum(container[i]) for i in range(n)]
    ball_sums = [sum(container[i][j] for i in range(n)) for j in range(n)]

    container_sums.sort()
    ball_sums.sort()

    return "Possible" if container_sums == ball_sums else "Impossible"

#Logic:
#In this function, I'm determining whether it's possible to organize the balls within the containers in a specific way. For each container, I calculate the total number of balls and for each type of ball, I calculate the total number in all containers. By sorting these sums, I can compare whether the total number of balls in each container matches the total number of each type of ball across all containers. If the sorted sums match, it's possible to organize the balls as required, and the function returns "Possible." Otherwise, it returns "Impossible." This approach checks the distribution of balls within containers to determine if a specific organization is achievable.