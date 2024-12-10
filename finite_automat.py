def transition(pattern, alphabet):
    m = len(pattern) 
    transition_function = {} 
    for q in range(m + 1):
        for a in alphabet:  
            k = min(m + 1, q + 2)
            while k > 0:
                k -= 1
                if pattern[:k] == (pattern[:q] + a)[-k:]:
                    break
            transition_function[(q, a)] = k

    return transition_function


def finite_automat(text, transition_function, pattern_length):
    n = len(text) 
    q = 0  
    for i in range(n):
        q = transition_function.get((q, text[i]), 0)
        if q == pattern_length:
            print("Pattern index:", i - pattern_length + 1)

text = "ababacababcabbc"
pattern = "abc" 
alphabet = set(text)  
transition_dict = transition(pattern, alphabet)  
finite_automat(text, transition_dict, len(pattern))