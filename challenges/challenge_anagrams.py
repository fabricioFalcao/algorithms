def is_anagram(first_string, second_string):
    first_sorted = quicksort_string(first_string)
    second_sorted = quicksort_string(second_string)

    if not first_sorted or not second_sorted:
        return (first_sorted, second_sorted, False)

    return (first_sorted, second_sorted, first_sorted == second_sorted)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def quicksort_string(word):
    arr = list(word.lower())
    quicksort(arr, 0, len(arr) - 1)
    sorted_word = "".join(arr)
    return sorted_word
