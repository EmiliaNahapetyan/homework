def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return f'index: {mid}'
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return "Not found."

arr = [2, 4, 6, 8, 10, 12, 14] 
x = 10 
print(binary_search(arr, x))
