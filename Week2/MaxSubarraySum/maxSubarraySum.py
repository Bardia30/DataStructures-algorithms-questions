#o(n)
class Solution:
    def maxSubArray(self, nums):
        maxSub = nums[0]

        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub



class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = max_sum

        for num in nums:
            current_sum = max(num + current_sum, num)
            max_sum = max(current_sum, max_sum)

        return max_sum





#brute force solution O(n^2)
def maxSubArray(nums):
    maxSum = float('-inf')

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            current_sum = sum(nums[i:j+1])
            if current_sum > maxSum:
                maxSum = current_sum

    return maxSum





#Divide and Conquer Solution
class Solution:
    def maxSubArray(self, nums):
        def helper(left, right):
            if left == right:
                return nums[left], nums[left], nums[left], nums[left]

            mid = (left + right) // 2

            l_lss, l_css, l_rss, l_ts = helper(left, mid)
            r_lss, r_css, r_rss, r_ts = helper(mid+1, right)

            css = max(l_css, l_ts + r_css)
            rss = max(r_rss, r_ts + l_rss)
            lss = max(l_lss, r_lss)
            ts = l_ts + r_ts

            return lss, css, rss, ts

        lss, css, rss, ts = helper(0, len(nums) - 1)
        return max(lss, css, rss)
