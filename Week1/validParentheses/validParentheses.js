//algorithm in python solution


const isValid = s => {
    pairs = {
        "]": "[",
        "}": "{",
        ")": "("
    }

    let openStack = [];

    for (let i = 0; i < s.length ; i++) {
        const currentParenthesis = s[i];
        
        //check to see if it is open
        if (pairs[currentParenthesis] === undefined) {
            openStack.push(currentParenthesis)
        } else {
            //check to see if closed isn't at beginning
            if (openStack.length !== 0) {
                //check to if corresponding open is the last item in openStack
                if (pairs[currentParenthesis] === openStack[openStack.length - 1]) {
                    openStack.pop();
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
    }

    
    if (openStack.length !== 0) {
        return false
    } else {
        return true;
    }
}

console.log(isValid("(])"))