#first solution, time O(N + M), space O(N+M)
def isAnagram(s, t):
    #hash map to count the s characters
    has_seen = {}
    # hash map to count the t characters
    has_seen2 = {}

    #if the lengths do not match, it is instantly a False return 
    if len(s) != len(t):
        return False
    
    for letter in range(len(s)):
        if s[letter] not in has_seen:
            has_seen[s[letter]] = 1
        else: 
            has_seen[s[letter]] += 1
    # print(has_seen)
            
    for letter in range(len(t)):
        if t[letter] not in has_seen:
            return False
        if t[letter] not in has_seen2:
            has_seen2[t[letter]] = 1
        else:
            has_seen2[t[letter]] += 1
    # print(has_seen2)
            
    for key in has_seen:
        if has_seen[key] != has_seen2[key]:
            return False
        
    return True

# print(isAnagram("rat", "car"))
# Time: O(nlogn), space: O(1)

def isAnagramSorted(s, t):
    return sorted(s) == sorted(t)
        
    
print(isAnagramSorted("anagram", "nagaram"))