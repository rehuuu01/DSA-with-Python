def subsets(nums):
    result = []

    def backtrack(index, path):
        if index == len(nums):
            result.append(path.copy())
            return

        # Not take current element
        backtrack(index + 1, path)

        # Take current element
        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()  # backtrack

    backtrack(0, [])
    return result


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print(subsets(nums))
