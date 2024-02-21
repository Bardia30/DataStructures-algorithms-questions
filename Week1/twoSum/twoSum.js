const twoNumberSum = (array, targetSum) => {
    //initialize an empty hash table (object), to keep track of already seen elements of the array
    //we want to find y, such that y = target - currentNum

    const seenHash = {}

    //traverse through the array
    for (let i = 0; i < array.length; i++) {
        let currentNum = array[i];
        let y = targetSum - currentNum;

        //check to see if y is in the hash already, if so we return currentNum and Y and we are done
        if (seenHash[y]) {
            return [y, currentNum]
        //if it is not in hash, we add it
        } else {
            seenHash[currentNum] = true
        }
    }
    return []
}

//second solution using sorting. 
const twoNumSum = (array, targetSum) => {
    array.sort((a, b) => a -b);

    let leftPointerIndex = 0;
    let rightPointerIndex = array.length -1;

    while (leftPointerIndex !== rightPointerIndex) {
        const leftPointer = array[leftPointerIndex];
        const rightPointer= array[rightPointerIndex];

        if (leftPointer + rightPointer === targetSum) {
            return [leftPointer, rightPointer]
        } else if (leftPointer + rightPointer < targetSum) {
            leftPointerIndex += 1;
        } else {
            rightPointerIndex = rightPointerIndex - 1;
        }
    }
    
    return [];
}


// console.log(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
console.log(twoNumSum([3, 5, -4, 8, 11, 1, -1, 6], 10))