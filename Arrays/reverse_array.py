# Function to reverse an array using two pointers
def reverse_array(arr):
    # Initialize pointers
    left = 0
    right = len(arr) - 1

    # Swap elements until pointers meet
    while left < right:
        # Swap the elements at left and right positions
        arr[left], arr[right] = arr[right], arr[left]

        # Move pointers towards the center
        left += 1
        right -= 1

    # Return the reversed array
    return arr


# Main execution block
if __name__ == "__main__":
    # Take number of elements from user
    n = int(input("Enter the number of elements in the array: "))
    
    # Initialize empty array
    arr = []

    # Take array elements as input
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)

    # Reverse and print the array
    reversed_arr = reverse_array(arr)
    print("Reversed array:", reversed_arr)
