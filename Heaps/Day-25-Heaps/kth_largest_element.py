import heapq

def findKthLargest(nums, k):
    """
    Find the kth largest element using a min heap of size k.
    Time: O(n log k)
    Space: O(k)
    """
    if k > len(nums) or k <= 0:
        return None

    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # 5
