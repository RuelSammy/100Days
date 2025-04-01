def bubble_sort(arr):
    for iter_num in range(len(arr) - 1, 0, -1):
        for idx in range(iter_num):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

arr1 = [19, 2, 31, 45, 6, 11, 121, 27]
bubble_sort(arr1)
print("Bubble Sort:", arr1)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res

arr2 = [64, 34, 25, 12, 22, 11, 90]
print("Merge Sort:", merge_sort(arr2))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        nxt_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > nxt_element:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = nxt_element

arr3 = [19, 2, 31, 45, 30, 11, 121, 27]
insertion_sort(arr3)
print("Insertion Sort:", arr3)
