def first_negative_integer(arr, k):
    if len(arr) < k or k <= 0:
        return None  # Edge case

    result = []
    neg_queue = []   # stores indices of negative numbers
    window_start = 0

    for window_end in range(len(arr)):
        # If current element is negative, add its index
        if arr[window_end] < 0:
            neg_queue.append(window_end)

        # When window size reaches k
        if window_end >= k - 1:
            # First negative in current window
            if neg_queue:
                result.append(arr[neg_queue[0]])
            else:
                result.append(0)

            # Remove elements going out of the window
            if neg_queue and neg_queue[0] == window_start:
                neg_queue.pop(0)

            window_start += 1  # Slide the window

    return result


if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    k = int(input("Enter the size of the window (k): "))

    result = first_negative_integer(arr, k)
    if result is None:
        print("Invalid input")
    else:
        print(f"The first negative integers in each window of size {k} are: {result}")
