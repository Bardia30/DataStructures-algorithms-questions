class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomHash = {}
        magHash = {}

        for char in ransomNote:
            if char in ransomHash:
                ransomHash[char] += 1
            else:
                ransomHash[char] = 1
            
        for char in magazine:
            if char in magHash:
                magHash[char] += 1
            else:
                magHash[char] = 1

        for key in ransomHash:
            if key not in magHash or ransomHash[key] > magHash[key]:
                return False
            
        return True
    
#better solution with only one dictionary
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #create a hash map of the magazine string
        magHash = {}

        for char in magazine:
            if char in magHash:
                magHash[char] += 1
            else:
                magHash[char] = 1

        #traverse through the ransomNote string,
        #if each char not in hash, return False or
        #if char in hash == 0, return false
        #otherwise, decrement
        for char in ransomNote:
            if char not in magHash or magHash[char] == 0:
                return False
            else:
                magHash[char] -= 1

        return True 