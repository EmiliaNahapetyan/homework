import math

def jump_search(arr, x):
    n = len(arr)
    m = int(math.sqrt(n))  

    prev = 0
    while prev < n and arr[min(m, n) - 1] < x:
        prev = m
        m += int(math.sqrt(n))
        if prev >= n:
            return -1 
    for i in range(prev, min(m, n)):
        if arr[i] == x:
           return ( f"index: {i}" )

    return "Not found" 


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 9

print(jump_search(arr, x))