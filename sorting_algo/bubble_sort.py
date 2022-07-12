# For array
def bubble_sort_array(arr):
    for j in range(len(arr) - 1):
        swapped = False
        for i in range((len(arr) - 1) - j):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swapped = True
        if not swapped:
            break

def bubble_sort_dict(elements, key):
    for j in range(len(elements)):
     for i in range(len(elements) - 1 - j):
             if( elements[i + 1][key] < elements[i][key] ):
                     temp = elements[i][key]
                     elements[i][key] = elements[i + 1][key]
                     elements[i + 1][key] = temp

if __name__ == '__main__':
    arr = [5, 9, 2, 1, 67, 34, 88, 34]
    
    bubble_sort_array(arr)
    print(arr)

    print()
    
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort_dict(elements, 'name')
    # bubble_sort(elements, 'transaction_amount')

    for i in elements:
        print(i)

