import heapq
from collections import Counter

def topKFrequent(nums, k):
    """
    Find k most frequent elements using min heap.
    Time: O(n log k)
    Space: O(n)
    """
    if k <= 0:
        return []

    freq_map = Counter(nums)
    min_heap = []

    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for freq, num in min_heap]


# Example
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))  # [1, 2]
