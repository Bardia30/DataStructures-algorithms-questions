const longestPalindrome = s => {
    const count = {};
    let length = 0;
    let oddCount = 0;

    for (let i = 0; i < s.length; i++) {
        const currChar = s[i]
        if (count[currChar] !== undefined) {
            count[currChar] += 1;
        } else {
            count[currChar] = 1;
        }
    }

    if (Object.keys(count).length === 1) {
        return count[s[0]];
    }

    for (let i = 0; i < Object.values(count).length; i++) {
        const currVal = Object.values(count)[i];

        if (currVal > 1) {
            if (currVal % 2 === 0) {
                length += currVal
            } else {
                oddCount++;
                length += currVal - 1;
            }
        } else {
            oddCount++;
        }
        
    }

    if (oddCount > 0) {
        return length + 1; 
    }
    return length;
}