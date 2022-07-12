# Noramal Binary search
def binary_search(arr, i):
    left = 0
    right = len(arr) - 1
    mid = (left+right)//2

    while left <= right:
        if i == arr[mid]:
            return True

        if i < arr[mid]:
            right = mid - 1

        if i > arr[mid]:
            left = mid + 1

        mid = (left + right)//2

    return False

# Binary search using recursion
def binary_search_rec(arr, i, left, right):
    if right < left:
        return -1
    
    mid = (left + right) // 2

    if i == arr[mid]:
        return True

    if i > arr[mid]:
        left = mid + 1
    
    elif i < arr[mid]:
        right = mid - 1
    
    return binary_search_rec(arr, i, left, right)
        

arr = [1, 10, 34, 35, 76, 87, 99]
i = 1
 
start = 0
end = len(arr)

# print(binary_search(arr, i))
x = (binary_search_rec(arr, i, start, end))
print(x)
