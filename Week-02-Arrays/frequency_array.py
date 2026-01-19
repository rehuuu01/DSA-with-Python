def frequency_array(arr):
    if not arr: 
        return {}
    frequency = {}

    # Count frequency of each element
    for element in arr:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

    return frequency
# Main execution block
if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    freq = frequency_array(arr)
    print("Frequency of each element:")
    print(freq)