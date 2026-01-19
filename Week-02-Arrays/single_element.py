def single_ele(arr):
    if not arr:
        return None

    element = {}

    # Step 1: Count frequency
    for i in arr:
        if i in element:
            element[i] += 1
        else:
            element[i] = 1

    # Step 2: Find element with frequency 1
    for key, value in element.items():
        if value == 1:
            return key

    return None
# Main execution block
if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    result = single_ele(arr)
    if result is not None:
        print("The single element in the array is:", result)
    else:
        print("No single element found in the array.")



