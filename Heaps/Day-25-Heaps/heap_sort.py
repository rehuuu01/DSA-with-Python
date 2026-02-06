def heapSort(arr):
    """
    Heap Sort (In-Place)
    Sorts the array in ascending order using a Max Heap.

    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """

    n = len(arr)

    # Step 1: Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (largest) to end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify reduced heap
        heapify(arr, i, 0)


def heapify(arr, n, i):
    """
    Maintains max heap property for subtree rooted at index i.
    """

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Example
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print(arr)  # [5, 6, 7, 11, 12, 13]
