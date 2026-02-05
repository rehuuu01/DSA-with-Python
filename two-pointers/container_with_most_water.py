def container_with_most_water(arr):
    left = 0
    right = len(arr) - 1
    max_area = 0

    while left < right:
        height = min(arr[left], arr[right])
        width = right - left
        current_area = height * width
        max_area = max(max_area, current_area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return max_area
if __name__ == "__main__":
    arr = list(map(int, input("Enter the heights of the lines separated by spaces: ").split()))
    result = container_with_most_water(arr)
    print(f"The maximum area of water that can be contained is: {result}")
