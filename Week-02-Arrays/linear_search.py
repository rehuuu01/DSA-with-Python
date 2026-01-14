def linear_search(arr, target):
    for i in range(len(arr)):
        # Check each element
        if arr[i] == target:
            # Target found, return index
            return i
    # Target not found
    return -1


if __name__ == "__main__":
    # Take array elements as input
    arr = list(map(int, input("Enter elements: ").split()))
    target = int(input("Enter element to search: "))
    result=linear_search(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")
    
