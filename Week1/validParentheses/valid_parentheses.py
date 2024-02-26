#create an pairs dictionary, key closed parenthesis, value open
#create a openStack
#traverse through the input string. 
#check if it is closed or open. 
#if open:
    #add to openStack
#if close:
    #check if length of stack is not 0 (to make sure closed is not at the beginning of string)
        #check if the corresponding open bracket is the last item is stack:
            # pop last item from stack
        #else: (not the last item in stack corresponds to he closed bracket)
            # return false
    # else: (closed is at the beginning of sentence)
    #     return false



def is_valid_parentheses(s):
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    open_stack = []

    for p in s:
        #if it is open
        if p not in pairs:
            open_stack.append(p)
        #if it is a closed bracket
        else:
            if len(open_stack) != 0:
                if pairs[p] == open_stack[-1]:
                    open_stack.pop()
                else:
                    return False
            else:
                return False
    
    if len(open_stack) == 0:
        return True 
    else:
        return False      


print(is_valid_parentheses("(])"))

