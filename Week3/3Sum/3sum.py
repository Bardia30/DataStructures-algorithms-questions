
class Solution:
    def threeSum(self, nums):
        
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            hasSeen = {}
            for j in range(i+1, len(nums)):
                complement = -nums[i] - nums[j]
                if complement in hasSeen:
                    ans.add(tuple(sorted((nums[i], nums[j], complement))))
                else:
                    hasSeen[nums[j]] = True
        return [list(triplet) for triplet in ans]
    
#better soln Time: o(nlogn) + o(n^2) => o(n^2), space: O(1) or O(n) (depends on the sorting)
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums [i -1]:
                continue

            #twoSum two pointer soln
            l, r = i +1, len(nums) -1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums [l - 1] and l < r:
                        l += 1
        return res
                