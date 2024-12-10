def str_palindrome(s):
    s = ''.join(s.split()).lower()
    odd_chars = set()

    for i in s:
        if i in odd_chars:
            odd_chars.remove(i)
        else:
            odd_chars.add(i)
    return len(odd_chars) <= 1

string = "A man a plan a canal  Panama"
if str_palindrome(string):
    print("String is palindrome.")
else:
    print("String is not palindrome.")
