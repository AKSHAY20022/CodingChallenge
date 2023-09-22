def twoNumberSum(array, targetSum):

    # Sort the array
    array.sort()
    
    # We can use two pointers technique Since the input array is sorted
    # the largest squared values can come from either the beginning or the end of the input array.
    left, right = 0, len(array) - 1
    
    while left < right:
        currentSum = array[left] + array[right]
        
        # If the current sum matches the target sum, return the pair of numbers
        if currentSum == targetSum:
            return [array[left], array[right]]
        # If the current sum is less than the target, move the left pointer to the right
        elif currentSum < targetSum:
            left += 1
        # If the current sum is greater than the target, move the right pointer to the left
        else:
            right -= 1
    
    # Returns an empty list if no pair is found
    return []

# Tester function
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum)) 
