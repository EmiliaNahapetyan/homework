def ternary_search(arr, x):
    left = 0  
    right = len(arr) - 1  
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == x: 
            return mid1
        if arr[mid2] == x: 
            return mid2

        if x < arr[mid1]:  
            right = mid1 - 1
        elif x > arr[mid2]:  
            left = mid2 + 1
        else:  
            left = mid1 + 1
            right = mid2 - 1

    return "not in arr" 

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 15

print("Element index:", ternary_search(arr, x))
