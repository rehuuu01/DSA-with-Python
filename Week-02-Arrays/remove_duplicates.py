def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0  # slow pointer (last unique index)

    for j in range(1, len(arr)):  # fast pointer
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1  # new length


# Main execution block
if __name__ == "__main__":
    # Take number of elements from user
    n = int(input("Enter the number of elements in the array: "))

    # Initialize empty array
    arr = []

    # Take array elements as input (unsorted allowed)
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)

    print("Original array:", arr)

    # STEP 1: Sort the array
    arr.sort()

    print("Sorted array:", arr)

    # STEP 2: Remove duplicates
    new_length = remove_duplicates(arr)

    # Print result
    print("Array after removing duplicates:", arr[:new_length])
    print("New length of the array:", new_length)
