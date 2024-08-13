# Function to rotate an array by d elements to the left

def rotate_array(arr, d):
    n = len(arr)
    d = d % n
    arr[:] = arr[d:] + arr[:d]

arr = [1, 2, 3, 4, 5]

d = 3

rotate_array(arr, d)

print("The array after rotation is", arr)