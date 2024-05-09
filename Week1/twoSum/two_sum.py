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

# print(twoNumSum([3, 5, -4, 8, 11, 1, -1, 6], 10))



#review 
#Solution 1: Brute Force, Double for loop, O(n^2) time, O(1) Space

def twoSumBrute(nums, target):
    for idx1, num1 in enumerate(nums):
        for idx2, num2 in enumerate(nums): 
            if num1 + num2 == target and idx1 != idx2: 
                return [idx1, idx2]


# print(twoSumBrute([3,3], 6))




#solution with sorting list, sliding window
def twoSumSort(nums, t):
    
    if not nums:
        return None
    
    sortedNums = sorted(nums)

    leftIdx = 0
    rightIdx = len(sortedNums) - 1
    
    # print(sortedNums)

    while leftIdx != rightIdx: 
        left = sortedNums[leftIdx]
        right = sortedNums[rightIdx]
        # print(f"left: {left}")
        # print(f"right: {right}")
        
        if left + right == t:
            firstResult = nums.index(left)
            secondResult = nums.index(right)
            if firstResult == secondResult: 
                #write code to replace scondResult with the second existing element in nums array
                secondResult = nums.index(right, firstResult + 1)
            return [firstResult, secondResult]

        elif left + right > t:
            rightIdx -= 1
            
        elif left + right < t: 
            leftIdx += 1
            
    return []



print(twoSumSort([3,3], 6))




#solution with using hash tables.
def twoSumHash(nums, target):
    if not nums:
        return None
    

    hasSeen = {}


    for num in nums: 
        if num in hasSeen:
            firstResult = nums.index(num)
            secondResult = nums.index(target - num)
            if firstResult == secondResult: 
                #write code to replace scondResult with the second existing element in nums array
                secondResult = nums.index(target - num, firstResult + 1)
            return [firstResult, secondResult]
        else:
            hasSeen[target - num] = True
    return []