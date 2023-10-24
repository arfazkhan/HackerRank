def organizingContainers(container):
    n = len(container)
    container_sums = [sum(container[i]) for i in range(n)]
    ball_sums = [sum(container[i][j] for i in range(n)) for j in range(n)]

    container_sums.sort()
    ball_sums.sort()

    return "Possible" if container_sums == ball_sums else "Impossible"