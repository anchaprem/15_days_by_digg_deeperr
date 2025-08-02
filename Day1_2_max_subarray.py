def max_subarray_better(arr):
    n = len(arr)
    prefix = [0] * (n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    max_sum = float('-inf')
    for i in range(n):
        for j in range(i, n):
            curr_sum = prefix[j+1] - prefix[i]
            max_sum = max(max_sum, curr_sum)
    return max_sum
print(max_subarray_better([-2,1,-3,4,-1,2,1,-5,4]))  