def twoNumberSum(array, targetSum):
    # Create an empty set to store numbers we've seen so far
    nums_seen = set()
    
    for num in array:
        # Calculate the complement of the current number with respect to the target sum
        complement = targetSum - num
        
        # If the complement is in the set, then we've found a pair that adds up to the target sum
        if complement in nums_seen:
            return [num, complement]
        
        # Add the current number to the set
        nums_seen.add(num)
    
    # Return an empty list if no pair is found
    return []

# Tester function
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))  
