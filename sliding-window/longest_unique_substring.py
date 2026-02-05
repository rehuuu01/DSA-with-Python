def longest_unique_substring(s):
    # Dictionary to store the last index where each character was seen
    char_index = {}

    # Left pointer of the sliding window
    left = 0

    # Stores the maximum length of substring found so far
    max_length = 0

    # Right pointer moves through the string character by character
    for right in range(len(s)):

        # If current character is already seen
        # AND it lies inside the current window
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move the left pointer to one position
            # after the previous occurrence of the character
            left = char_index[s[right]] + 1

        # Update the last seen index of the current character
        char_index[s[right]] = right

        # Calculate current window length
        current_window_length = right - left + 1

        # Update maximum length if current window is larger
        max_length = max(max_length, current_window_length)

    # Return the maximum length of substring with unique characters
    return max_length


if __name__ == "__main__":
    # Take input string from the user
    s = input("Enter the string: ")

    # Call the function to find longest unique substring length
    result = longest_unique_substring(s)

    # Print the result
    print(f"The length of the longest substring with all unique characters is: {result}")
