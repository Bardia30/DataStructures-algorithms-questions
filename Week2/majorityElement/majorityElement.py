#o(n) time and space
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

#solution with O(1) space
class Solution:
    def majorityElement(self, nums):
        
        count = 0
        answer = None

        for num in nums:
            if count == 0:
                answer = num
            
            if num == answer:
                count += 1
            else:
                count -= 1

        return answer