def left_rotate_by_k(arr, k):
    n = len(arr)

    if n == 0:
        return arr

    # Handle cases where k >= n
    k = k % n

    # Helper function to reverse part of array
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Step 1: Reverse first k elements
    reverse(0, k - 1)

    # Step 2: Reverse remaining elements
    reverse(k, n - 1)

    # Step 3: Reverse whole array
    reverse(0, n - 1)

    return arr
# Main execution block
if __name__ == "__main__":
  arr=list(map(int,input("Enter elements: ").split()))
  k=int(input("Enter number of positions to left rotate: "))
  result = left_rotate_by_k(arr, k)
  print("Array after left rotation by", k, "positions:", result)
  