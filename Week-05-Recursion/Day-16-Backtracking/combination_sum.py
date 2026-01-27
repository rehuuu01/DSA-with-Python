def combination_sum(candidates, target):
    result = []

    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path.copy())
            return
        if current_sum > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, current_sum + candidates[i])
            path.pop()  # backtrack

    backtrack(0, [], 0)
    return result


if __name__ == "__main__":
    candidates = list(map(int, input("Enter candidates: ").split()))
    target = int(input("Enter target: "))
    print(combination_sum(candidates, target))
