def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j  in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            print("Array is already sorted!")
            break
    return arr

arr=[3, 4, 5, 7, 9, 10, 22, 99]
print(bubble_sort(arr))
