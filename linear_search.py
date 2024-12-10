def linear_search(arr, x):
    m=len(arr)
    for ind in range(m):
        if arr[ind] == x:
            return ind
    return 'Not found.'

arr = [5, 3, 7, 10, 15] 
x = 10
print(linear_search(arr,x))
