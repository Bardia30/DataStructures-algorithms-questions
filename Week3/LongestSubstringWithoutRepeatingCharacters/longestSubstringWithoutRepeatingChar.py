#Neetcode, returns the length only
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[r])
            res = max(res, r - left +1)
        return res
    
#returns the actual substring
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = {}
        startIdx = 0
        longest = ""
        for i in range(len(s)):
            if s[i] in hashSet:
                startIdx = max(startIdx, hashSet[s[i]] + 1)
                
            hashSet[s[i]] = i
            if len(s[startIdx:i+1]) > len(longest):
                longest = s[startIdx:i+1]

        return longest