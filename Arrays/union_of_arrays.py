def union_of_arrays(arr1, arr2):
    union_set = set()

    # Add elements from first array
    for element in arr1:
        if element not in union_set:
            union_set.add(element)

    # Add elements from second array
    for element in arr2:
        if element not in union_set:
            union_set.add(element)

    return list(union_set)


if __name__ == "__main__":
    arr1 = list(map(int, input("Enter elements of first array: ").split()))
    arr2 = list(map(int, input("Enter elements of second array: ").split()))

    result = union_of_arrays(arr1, arr2)
    print("Union of both arrays:", result)
