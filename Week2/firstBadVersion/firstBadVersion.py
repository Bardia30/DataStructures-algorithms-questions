# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        while n > 0:
            if isBadVersion(n):
                n = n - 1
            else:
                return n + 1
        return 1



#binary search solution 
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        result = n

        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result