class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        length = 0
        oddCount = 0

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        if len(count) == 1:
            return count[s[0]]
        
        for key in count:
            if count[key] > 1:
                if count[key] % 2 == 0:
                    length += count[key]
                else:
                    oddCount += 1
                    length += count[key] - 1
            else:
                oddCount += 1

        if oddCount > 0:
            return length + 1
        return length