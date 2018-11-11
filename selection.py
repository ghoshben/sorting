def selectionsort(arr):
    n = len(arr) - 1
    for i in range(0, n):
        for j in range(0, n - i):
            if arr[j] > arr[j + 1]:
                maxeliment = j  # finding the largest element
            else:
                maxeliment = j + 1  # finding the largest element
            arr[n - i], arr[maxeliment] = arr[maxeliment], arr[n - i]  # swapping the largest element with last 
            # element of the array 
    print(arr)


a = [1, 2, 5, 4, 3]
selectionsort(a)
