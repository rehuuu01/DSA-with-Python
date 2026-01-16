def move_zeros_to_end(arr):
    if not arr:
        return arr
    n = len(arr)
    # Move all non-zero elements to the front
    j=0 # Count of non-zero elements
    for i in range(0,len(arr)):
        if arr[i] != 0:
            arr[j]=arr[i]
            j+=1
    # Fill remaining positions with zeros
    for i in range(j,len(arr)):
       arr[i]=0
    return arr


# Main execution block
if __name__ == "__main__":
    arr = list(map(int, input("Enter elements: ").split()))
    result = move_zeros_to_end(arr)
    print("Array after moving zeros to the end:", result)

    

    


