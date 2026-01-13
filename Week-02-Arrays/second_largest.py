# Function to find the second largest element in an array
def find_second_largest(arr):
    # If array has less than 2 elements, second largest is not possible
    if len(arr) < 2:
        return "Array must have at least two elements"

    # Initialize largest and second largest to negative infinity
    largest = second_largest = float('-inf')

    # Traverse each element in the array
    for num in arr:
        # If current number is greater than largest
        if num > largest:
            # Update second largest before updating largest
            second_largest = largest
            largest = num
        
        # If number is less than largest but greater than second largest
        elif num != largest and num > second_largest:
            second_largest = num

    # If second largest was never updated, it doesn't exist
    if second_largest == float('-inf'):
        return "No second largest element"

    # Return the second largest value
    return second_largest


# Main execution block
if __name__ == "__main__":
    # Take array size from user
    n = int(input("Enter the number of elements in the array: "))
    
    # Initialize empty array
    arr = []

    # Take elements from user
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)

    # Find and print the second largest element
    result = find_second_largest(arr)
    print(f"The second largest element in the array is: {result}")
