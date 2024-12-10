# Step 1: Create the bad character shift table
def bad_character_shift(pattern):
    m = len(pattern)
    shift = {}

    # Initially, set all characters' shift value to the length of the pattern
    for char in pattern:
        shift[char] = m

    # For each character in the pattern, set the shift value based on the position
    for i in range(m - 1):
        shift[pattern[i]] = m - 1 - i

    return shift

# Step 2: Implement the Boyer-Moore string search
def boyer_moore_search(text, pattern):
    n = len(text)  # Length of the text
    m = len(pattern)  # Length of the pattern

    # Step 2.1: Generate the bad character shift table
    shift = bad_character_shift(pattern)

    i = m - 1  # Start from the last character of the text
    j = m - 1  # Start from the last character of the pattern

    found = False  # Flag to check if pattern is found

    # Step 2.2: Loop through the text to find the pattern
    while i < n:
        if text[i] == pattern[j]:  # If characters match
            if j == 0:  # If the entire pattern is matched
                print(f"Pattern found at index {i}")
                found = True
                i += m  # Skip ahead to continue searching
                j = m - 1  # Reset pattern index
            else:
                i -= 1  # Move the text pointer to the left
                j -= 1  # Move the pattern pointer to the left
        else:  # If characters do not match
            if text[i] in shift:
                i += shift[text[i]]  # Use the bad character shift table
            else:
                i += m  # If the character is not in the pattern, shift by the full length of the pattern
            j = m - 1  # Reset the pattern pointer to the end

    if not found:
        print("Pattern not found in the text.")  # If no match is found

# Example usage of the Boyer-Moore algorithm
text = "abbabcababcacbabc"
pattern = "ababc"
boyer_moore_search(text, pattern)

# Example where the pattern is not found in the text
pattern = "xyz"
boyer_moore_search(text, pattern)
