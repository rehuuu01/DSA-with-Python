def min_subset_sum_diff(arr):
    total_sum = sum(arr)
    n = len(arr)

    # 1D DP
    dp = [False] * (total_sum + 1)
    dp[0] = True

    for num in arr:
        for j in range(total_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    # Find minimum difference
    min_diff = float('inf')

    for s1 in range(total_sum // 2 + 1):
        if dp[s1]:
            diff = abs(total_sum - 2 * s1)
            min_diff = min(min_diff, diff)

    return min_diff


# ✅ Example Usage
if __name__ == "__main__":
    arr = [1, 6, 11, 5]
    result = min_subset_sum_diff(arr)
    
    print("Array:", arr)
    print("Minimum Subset Sum Difference:", result)