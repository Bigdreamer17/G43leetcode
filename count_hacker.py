def countingSort(arr):
    # Write your code here
    counting_arr = [0] * 100
    for i in arr:
        counting_arr[i] += 1
    return counting_arr