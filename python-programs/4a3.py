def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    merge = lambda l, r: sorted(l + r)
    return merge(merge_sort(left), merge_sort(right))

if __name__ == "__main__":
    input_list = [12, 11, 13, 5, 6, 7]
    sorted_list = merge_sort(input_list)
    print("Sorted list:", sorted_list)
