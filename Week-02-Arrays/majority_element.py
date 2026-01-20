def majority_element(arr):
    n=len(arr)
    majority=arr[0]
    votes=1
    for i in range(1,n):
        if votes==0:
            majority=arr[i]
        if arr[i]==majority:
            votes+=1
        else:
            votes-=1
        return majority
# Main execution block
if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

    result = majority_element(arr)
    print("Majority element is:", result)    