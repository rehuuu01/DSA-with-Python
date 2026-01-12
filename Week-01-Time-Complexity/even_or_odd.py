# Function to check whether a number is even or odd
def is_even(n):
    # If the number is less than or equal to 0, it's not valid
    if n <= 0:
        return "Enter a valid number"
    
    # If the number is divisible by 2, it is even
    elif n % 2 == 0:
        return "Even"
    
    # Otherwise, the number is odd
    else:
        return "Odd"


# This block runs only when the file is executed directly
if __name__ == "__main__":
    # Take input from the user
    n = int(input("Enter a number: "))
    
    # Call the function and print the result
    print(is_even(n))

       
