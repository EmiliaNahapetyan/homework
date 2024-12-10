def longest_palindrome(s):
    longest = ""  
    m=len(s)
    for i in range(m):
        for j in range(i + 1, m + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                if len(substring) > len(longest):
                    longest = substring 

    return longest

text = "bababd"
print("Longest Palindrome:",longest_palindrome(text) )
