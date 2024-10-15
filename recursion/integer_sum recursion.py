def recursiveSumEven(arr, idx=0):
    if idx >= len(arr):
        return 0
    else:
        return arr[idx] + recursiveSumEven(arr, idx + 2)
