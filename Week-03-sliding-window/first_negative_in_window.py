def frist_negative_integer(arr, k):
    n = len(arr)
    result = []
    neg_index = []

    # Process the first window
    for i in range(k):
        if arr[i] < 0:
            neg_index.append(i)

    # Process the rest of the windows
    for i in range(k, n):
        # Append the first negative integer of the previous window
        if neg_index:
            result.append(arr[neg_index[0]])
        else:
            result.append(0)

        # Remove elements that are out of this window
        while neg_index and neg_index[0] <= i - k:
            neg_index.pop(0)

        # Add the current element if it is negative
        if arr[i] < 0:
            neg_index.append(i)

    # Append the first negative integer of the last window
    if neg_index:
        result.append(arr[neg_index[0]])
    else:
        result.append(0)

    return result
if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    k = int(input("Enter the size of the window (k): "))
    # Call the function and print the result
    result = frist_negative_integer(arr, k)
    print(f"The first negative integers in each window of size {k} are: {result}")