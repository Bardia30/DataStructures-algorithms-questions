class Solution:
    def majorityElement(self, nums):
        count = {}


        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for key in count:
            if count[key] > (len(nums)/2):
                return key
