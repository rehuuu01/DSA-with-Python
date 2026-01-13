# Function to find the maximum element in an array
def find_max(arr):
    # Assume the first element is the maximum
    max_val = arr[0]

    # Traverse each element in the array
    for num in arr:
        # If current element is greater than max_val, update it
        if num > max_val:
            max_val = num

    # Return the maximum value found
    return max_val


# This block runs only when the file is executed directly
if __name__ == "__main__":
    # Take number of elements from the user
    n = int(input("Enter the number of elements in the array: "))
    
    # Initialize empty array
    arr = []

    # Take array elements as input
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)

    # Find and print the maximum element
    max_element = find_max(arr)
    print(f"The maximum element in the array is: {max_element}")
