def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while (j >= 0 and key < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = key
arr = [9,8,4,3,5]
print("unsorted arraay:",arr)
insertion_sort(arr)
print("sorted arrray:",arr)