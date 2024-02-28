class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        
        newA = ""
        newB = ""

        if len(a) != len(b):
            diffLengths = abs(len(a) - len(b))
            if len(a) < len(b):
                newA = "0" * diffLengths + a
                newB = b
            else:
                newA = a
                newB = "0" * diffLengths + b
        else:
            newA = a
            newB = b
        
        print(f"a: {newA}")
        print(f"b: {newB}")
        


        for i in range(len(newA) - 1, -1, -1):
            currA = newA[i]
            currB = newB[i]
            

            addition = int(currA) + int(currB) + carry
            # if addition == 0 or addition == 1:
            #     result = str(addition) + result
            #     carry = 0
            # else:
            #     result = "0" + result
            #     carry = 1
            char = str(addition % 2)
            result = char + result
            carry = addition // 2
        if carry == 1:
            return "1"+result
        return result
    
solution = Solution()
print(solution.addBinary("1111", "1111"))


#cleaner solution
class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total %2)
            res = char + res
            carry = total //2

        if carry:
            res = "1" + res
        return res