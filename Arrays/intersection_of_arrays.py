def intersection_of_arrays(arr1, arr2):
    intersection_set = set()

    # Convert second array to a set for faster lookup
    set_arr2 = set(arr2)

    # Find common elements
    for element in arr1:
        if element in set_arr2:
            intersection_set.add(element)

    return list(intersection_set)
if __name__ == "__main__":
    arr1 = list(map(int, input("Enter elements of first array: ").split()))
    arr2 = list(map(int, input("Enter elements of second array: ").split()))

    result = intersection_of_arrays(arr1, arr2)
    print("Intersection of both arrays:", result)