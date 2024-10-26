def shell_sort(arr):
    n = len(arr)
    gap = n // 2 
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]  
            j = i  
            
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap] 
                j -= gap 
            arr[j] = temp  
        
        gap //= 2 
    
    return arr

arr = [39, 12, 85, 72, 10, 2, 18]
print(shell_sort(arr))
