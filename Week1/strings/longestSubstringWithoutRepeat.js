//takes in a string as input
//outputs the longest substring without duplication

//e.g.

//input = 'clementisacap'
//output = 'mentisac'


//solution


const longestSubstringWithoutDuplication = (string) => {
    const lastSeen = {}
    //longest as in an array that contains the starting and ending indeces of the longest substring
    let longest = [0, 1];
    let startIndex = 0;


    for (let i = 0; i < string.length; i++) {
        let currentChar = string[i];

        if (lastSeen[currentChar] !== undefined) {
            startIndex = Math.max(startIndex, lastSeen[currentChar] + 1)
        }

        if (longest[1] - longest[0]  < i + 1  - startIndex) {
            longest = [startIndex, i + 1]
        }

        lastSeen[currentChar] = i
    }

    return string.substring(longest[0], longest[1])
}



console.log(longestSubstringWithoutDuplication("clementisac"))

