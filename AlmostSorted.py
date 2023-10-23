#https://www.hackerrank.com/challenges/almost-sorted/problem?isFullScreen=true
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

#Logic:
# In this code, we begin by checking if the input array arr is sorted in its current state. We do this by comparing it to a version of itself that has been sorted, which we call is_sorted. If we find that the two arrays are identical, that's a clear sign that our input array is already sorted, and we print 'yes' to confirm this. But if arr is not sorted, we proceed to identify the specific positions where it differs from the sorted version. These differing positions are stored in the diff_indices list. Our next step is to examine these differing indices: if there are exactly two of them, it implies that a simple swap operation can sort the array. In such a case, we print 'yes' and provide the details of the swap operation. However, if there are more than two differing indices, a swap won't work, so we attempt to reverse a segment of the array and check if the result is sorted. If it is, we print 'yes' and specify the reverse operation. If none of these conditions are met, we conclude that it's not possible to sort the array with a minimal number of operations, and we print 'no'