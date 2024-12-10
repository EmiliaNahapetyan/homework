def failure_func(p):
    m = len(p)
    F = [0] * m
    len_p = 0
    j = 1
    
    while j < m:
        if p[j] == p[len_p]:
            len_p += 1
            F[j] = len_p
            j += 1
        elif len_p > 0:
            len_p = F[len_p - 1]
        else:
            F[j] = 0
            j += 1

    return F

def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)

    F = failure_func(pattern)

    i = 0
    j = 0  
    found = False 

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:  
            print(f"Pattern found at index: {i - j}")
            found = True 
            j = F[j - 1]  
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = F[j - 1]  
            else:
                i += 1  

    if not found:  
        print("Pattern not found.")

text = "abbabcababcacbabc"
pattern = "ababc"
kmp_search(text, pattern)


