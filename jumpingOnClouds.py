def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100 
    current_cloud = 0

    while True:
        current_cloud = (current_cloud + k) % n
        energy -= 1

        if c[current_cloud] == 1:
            energy -= 2
        if current_cloud == 0:
            break  
    return energy