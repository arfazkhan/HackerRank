def circularArrayRotation(a, k, queries):
    n = len(a)
    effective_rotation = k % n
    rotated_positions = [(i - effective_rotation) % n for i in queries]
    result = [a[pos] for pos in rotated_positions]
    
    return result
