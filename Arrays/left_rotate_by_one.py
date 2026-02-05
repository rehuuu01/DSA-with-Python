def left_rotate_by_one(arr):
    n = len(arr)

    if n == 0:
        return arr

    # Step 1: store first element
    first = arr[0]

    # Step 2: shift elements to the left
    for i in range(1, n):
        arr[i - 1] = arr[i]

    # Step 3: place first element at the end
    arr[n - 1] = first

    return arr


# Main execution block
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        arr.append(int(input(f"Enter element {i+1}: ")))

    print("Original array:", arr)

    left_rotate_by_one(arr)

    print("Array after left rotation by one:", arr)
