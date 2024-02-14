const isAnagram = (s, t) => {
    const hasSeen = {};
    const hasSeen2 = {};

    if (s.length !== t.length) {
        return false;
    }

    for (let i = 0; i < s.length; i++) {
        let currentChar = s[i]
        if (hasSeen[currentChar] === undefined) {
            hasSeen[currentChar] = 1;
        } else {
            hasSeen[currentChar] += 1;
        }
    }
    // console.log(hasSeen)

    for (let i = 0; i < t.length; i++) {
        let currentChar = t[i];
        if (hasSeen[currentChar] === undefined) {
            return false;
        }
        if (hasSeen2[currentChar] === undefined) {
            hasSeen2[currentChar] = 1;
        } else {
            hasSeen2[currentChar] += 1;
        }
    }
    // console.log(hasSeen2)

    for (let i = 0; i < Object.keys(hasSeen).length; i++) {
        let currentKey = Object.keys(hasSeen)[i];
        if (hasSeen[currentKey] !== hasSeen2[currentKey]) {
            return false;
        }
    }

    return true;
}



console.log(isAnagram("anagram", "nagaram"))



// console.log(isValidAnagramSorted("anagram", "nagaram"))