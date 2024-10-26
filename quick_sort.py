def quick_sort(arr):
    n=len(arr)
    if n==0:
        return []
    pivot=arr[n//2]
    left=[]
    middle=[]
    right=[]
    for i in arr:
        if  i<pivot:
            left.append(i)
        elif i==pivot:
            middle.append(i)
        elif i>pivot:
            right.append(i)

    return quick_sort(left) + middle + quick_sort(right)

arr=[2, 9, 13, 24, 7, 6, 1, 3, 4]
print(quick_sort(arr))
