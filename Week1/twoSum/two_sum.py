def twoNumberSum(array, targetSum):
    #we want to find y such that y = 10 - currentNum
    #create an empty hash table

    seen_hash = {}

    #loop through the array 
    for currentNum in array:
        #finding y
        y = targetSum - currentNum
        #if y is already in hash table we are done. 
        if y in seen_hash:
            return [y, currentNum]
        else:
            #if y is not in hash table, we add it 
            seen_hash[currentNum] = True
    return []



# print(twoNumberSum([4,6, 1], 5))


#second solution using sorting

def twoNumSum(array, targetSum): 
    #first we sort the array: O(Nlog(N))
    array.sort()

    #assign left and right pointers
    left_pointer_index = 0
    right_pointer_index = len(array) - 1
    
    # we create a while loop to run as long as the indeces are not equal to each other, if they are equal means that we have checked everything, adn there is no pair
    while left_pointer_index != right_pointer_index:

        left_pointer = array[left_pointer_index]
        right_pointer = array[right_pointer_index]

        if left_pointer + right_pointer == targetSum:
            return [left_pointer, right_pointer]
        #if the sum is bigger than the target we have to move the left pointer to the left
        elif left_pointer + right_pointer > targetSum:
            right_pointer_index -= 1
        #if the sum is smaller than the target, we have to move the right pointer to the right
        else:
            left_pointer_index += 1
    return []

print(twoNumSum([3, 5, -4, 8, 11, 1, -1, 6], 10))


