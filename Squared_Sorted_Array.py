def sorted_squared_array(array):
    # The length of the input array
    n = len(array)
    
    # An array initialized with 0 to store the squares of the input elements
    squared = [0] * n
    
    # I used two pointers technique, Since the input array is sorted, 
    # the largest squared values can come from either the beginning or the end of the input array.
    left, right = 0, n - 1
    
    # We'll start filling the squared array from the end since
    # squares of the numbers could be larger and we want to keep them sorted
    for i in range(n - 1, -1, -1):
        
        # If the absolute value of the left pointer is greater than the right pointer
        if abs(array[left]) > abs(array[right]):
            squared[i] = array[left] ** 2
            left += 1
        else:
            squared[i] = array[right] ** 2
            right -= 1
            
    return squared

# Test the function
array = [1, 2, 3, 5, 6, 8, 9]
print(sorted_squared_array(array))  # Expected output: [1, 4, 9, 25, 36, 64, 81]


