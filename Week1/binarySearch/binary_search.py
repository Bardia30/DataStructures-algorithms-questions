#input: a sorted array, item to be found inside the array
def binary_search(list, item):
    #pointers 
    low = 0
    high = len(list) -1

    while low <= high:
        mid = (low + high) // 2 
        guess = list[mid]

        if guess == item: 
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# print(binary_search([1,3,5,7,9], -1))



def search(nums, t):
    left = 0
    right = len(nums) -1


    while left <= right:
        mid = (left +right )// 2
        
        if nums[mid] == t:
            return mid
        if nums[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

print(search([5], 5))