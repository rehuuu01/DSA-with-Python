def reverse_array(arr, start, end):
    # Base case
    if start >= end:
        return

    # Swap elements
    arr[start], arr[end] = arr[end], arr[start]

    # Recursive call
    reverse_array(arr, start + 1, end - 1)


if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    reverse_array(arr, 0, len(arr) - 1)
    print("Reversed array:", arr)
