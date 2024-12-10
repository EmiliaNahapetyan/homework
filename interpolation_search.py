def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= x <= arr[high]:
        pos = low + ((x - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == x:
            return f"Found at index: {pos}"
        elif arr[pos] < x:
            low = pos + 1  
        else:
            high = pos - 1  
    return "Not found"

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
x = 50

print(interpolation_search(arr, x))
