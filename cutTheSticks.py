def cutTheSticks(arr):
    result = [] 

    while arr:
        result.append(len(arr))
        min_length = min(arr)
        arr = [stick - min_length for stick in arr if stick - min_length > 0]

    return result