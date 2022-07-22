def swap_ele(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    pivot = start 
    end = len(elements) - 1
    start = pivot + 1

    while start < end:

        while start < len(elements) and elements[start] <= elements[pivot]:
            start += 1 

        while elements[end] > elements[pivot]:
            end -= 1

        if start < end:
            # elements[start], elements[end] = elements[end], elements[start]
            swap_ele(start, end, elements)
    
    # elements[end], elements[pivot] = elements[pivot], elements[end]
    swap_ele(end, pivot, elements)

    return end


def quick_sort(elements, start, end):
    if start < end:
        partition_idx = partition(elements, start, end)
        quick_sort(elements, start, partition_idx - 1)   # For left partition
        quick_sort(elements, partition_idx + 1, end)     # For Right partition
    

if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
