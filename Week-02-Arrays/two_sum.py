def two_sum(num, target):
    num_map={}
    n=len(num)
    for i in range(0,n):
        remaining=target - num[i]
        if remaining in num_map:
            return (num_map[remaining],i)
        num_map[num[i]]=i
    return (-1,-1)
# Main execution block
if __name__ == "__main__":
    num = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    target = int(input("Enter the target sum: "))
    result = two_sum(num, target)
    if result != (-1, -1):
        print(f"Indices of the two numbers that add up to {target} are: {result}")
    else:
        print("No two numbers add up to the target sum.")