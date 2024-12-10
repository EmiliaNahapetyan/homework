def exponential_search(arr, x):
    n = len(arr)
    i = 1
    while i < n and arr[i] < x:
        if arr[0] == x:
            return f" index 0"
        i *= 2

    return binary_search(arr, x)


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

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
x = 16

print(exponential_search(arr, x))
