def is_sorted(arr):
    # Traverse till second last element
    for i in range(len(arr) - 1):
        # If current element is greater than next, array is not sorted
        if arr[i] > arr[i + 1]:
            return False
    # If no violation found, array is sorted
    return True


if __name__ == "__main__":
    
    # Take number of elements from the user
    n = int(input("Enter the number of elements in the array: "))
    
    # Initialize empty array
    arr = []

    # Take array elements as input
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)

    # function call to check if array is sorted
    sorted_arr =is_sorted(arr)
    if sorted_arr:
        print("The array is sorted in non-decreasing order.")
    else:
        print("The array is not sorted.")
    # Find and print whether the array is sorted