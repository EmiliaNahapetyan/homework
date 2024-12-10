def palindrome(x):
    x = x.lower()
    rev_x = x[::-1]
    
    if x == rev_x:
        print("The word is a palindrome!")
    else:
        print("The word is not a palindrome.")

x = "madam"
palindrome(x)

