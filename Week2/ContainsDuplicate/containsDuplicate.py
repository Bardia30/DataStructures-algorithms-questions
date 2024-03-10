#using hash map, O(n) T + S
class Solution:
    def containsDuplicate(self, nums):
        count = {}

        for num in nums:
            if num in count:
                return True
            else:
                count[num] = 1
        return False
    
#soln # 2 using sets
class Solution:
    def containsDuplicate(self, nums):
        set_nums = set(nums)

        if len(set_nums) == len(nums):
            return False
        else:
            return True
        
#soln #3 using sorting
class Solution:
    def containsDuplicate(self, nums):
        nextIdx = 1
        nums.sort()
        for num in nums:
            if nextIdx < len(nums):
                if nums[nextIdx] == num:
                    return True
                nextIdx += 1

        return False