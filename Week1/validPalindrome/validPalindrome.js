const isPalindrome = (s) => {
    const newString = s.toLowerCase().replace(/[^a-zA-Z0-9]/g, '');

    let left = 0;
    let right = newString.length -1;


    while (left < right) {
        if (newString[left] !== newString[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}



console.log(isPalindrome("race a car"));