def bubblesort(arr):
    n = len(arr) - 1  # determinging the given array length
    for i in range(0, n):  # iterate through the whole list
        for j in range(0, n - i):  # on the i-th iteration
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # if the left element in larger then swap them
    print(arr)


a = [5, 2, 3, 1, 7]
bubblesort(a)
