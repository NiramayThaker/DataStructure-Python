def swap_ele(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


def partition(elements, start, end):
    p_idx = start
    pivot = elements[end]

    for i in range(start, end):
        if elements[i] <= pivot:
            swap_ele(i, p_idx, elements)
            p_idx += 1

    swap_ele(p_idx, i, elements)

    return p_idx


def quick_sort(elements, start, end):
    if len(elements) == 1:
        return 
        
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, pi + 1, end)
        quick_sort(elements, start, pi - 1)


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]

    start = 0
    end = len(elements) - 1

    quick_sort(elements, start, end)
    print(elements)
