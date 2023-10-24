def almostSorted(arr):
    n = len(arr)
    is_sorted = sorted(arr)
    
    if arr == is_sorted:
        print("yes")
        return

    diff_indices = [i for i in range(n) if arr[i] != is_sorted[i]]

    if len(diff_indices) == 2:
        print("yes")
        print("swap", diff_indices[0] + 1, diff_indices[1] + 1)
        return

    reverse_segment = arr[:diff_indices[0]] + arr[diff_indices[-1]:diff_indices[0]-1:-1] + arr[diff_indices[-1]+1:]

    if reverse_segment == is_sorted:
        print("yes")
        print("reverse", diff_indices[0] + 1, diff_indices[-1] + 1)
        return
    
    print("no")