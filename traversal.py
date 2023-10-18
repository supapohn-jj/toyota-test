def inorderTraversal(arr):
    if isinstance(arr, list):
        for sublist in arr:
            yield from inorderTraversal(sublist)
    elif isinstance(arr, int):
        yield arr

arr1 = [[[6]], [1, 3], []]
generator1 = inorderTraversal(arr1)
for value in generator1:
    print(value) 

arr2 = []
generator2 = inorderTraversal(arr2)
for value in generator2:
    print(value)  
