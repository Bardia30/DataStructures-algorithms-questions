def isPalindrome(s):
    import re



    pattern = r"[^a-zA-Z0-9]"


    new_string = re.sub(pattern, "", s.lower())

    print(new_string)
    left = 0

    right = len(new_string) -1


    while left < right:
        if new_string[left] != new_string[right]:
            return False
        left += 1
        right -= 1

    return True 


print(isPalindrome("ab_a"))

#other solutions given the input is only lower case letters
#O(n^2) time/ O(n) space

def isPalindrome2(string):
    reversedString = ""

    for i in reversed(range(len(string))):
        reversedString += string[i]

    return string == reversedString

# O(n) time / O(n) space

def isPalindrome(string):
    reversedChars = []

    for i in reversed(range(len(string))):
        reversedChars.append(string[i])

    return string == "".join(reversedChars)



#recursive solution
# O(n) time / O(n) space
def isPalindromeRecursive(string, i=0):
    j = len(string) -1 - i

    #in one line
    # return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)

    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindromeRecursive(string, i + 1)


#best solution
#O(n) time / o(1) space. For the leetcode question, the space is however still O(N)
def isPalindromeBest(string):

    leftIdx = 0
    rightIdx = len(string) - 1

    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1

    return True