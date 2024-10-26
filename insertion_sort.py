def insertion_sort(arr):
    n=len(arr)
    for i in range(1, n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j -= 1
        arr[j+1]=key

    return arr

arr=[2, 8, 1, 12, 3, 11, 10, 6, 4, 9, 5, 7]
print(insertion_sort(arr))