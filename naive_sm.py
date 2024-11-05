def naive_sm(txt, pat):
    n=len(txt)
    m=len(pat)
    result = -1
    for i in range(n):
        count = 0
        for j in range(m):
            if pat[j]==txt[i]:
                count += 1
                i += 1
            else:
                break
        if count==m:
            result = i-m 
            return result
    return result


txt= "ababbbaababbabba"
pat="abba"
print(naive_sm(txt, pat))

