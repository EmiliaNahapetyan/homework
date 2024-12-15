def palindrome(s):
    s = s.replace(" ", "").lower()
    char_count = {}
    for i in s:
        char_count[i] = char_count.get(i, 0) + 1
    
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    return odd_count <= 1

s = "anita lava la tina"
if palindrome(s):
    print("նախադասությունը կարող է դառնալ պալինդրոմ:")
else:
    print("նախադասությունը չի կարող դառնալ պալինդրոմ:")
