def hurdleRace(k, height):
    max_hurdle = max(height)
    doses_needed = max_hurdle - k
    return max(0, doses_needed)