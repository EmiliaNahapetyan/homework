def bad_character_shift(pattern):
    m = len(pattern)
    shift = {}
    for char in pattern:
        shift[char] = m
    for i in range(m - 1):
        shift[pattern[i]] = m - 1 - i
    return shift

def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    shift = bad_character_shift(pattern)
    i = m - 1
    j = m - 1
    found = False
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                print(f"Pattern found at index {i}")
                found = True
                i += m
                j = m - 1
            else:
                i -= 1
                j -= 1
        else:
            if text[i] in shift:
                i += shift[text[i]]
            else:
                i += m
            j = m - 1
    if not found:
        print("Pattern not found in the text.")

text = "abbabcababcacbabc"
pattern = "ababc"
boyer_moore_search(text, pattern)
