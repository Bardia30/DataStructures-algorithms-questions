/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const magHash = {};
    
    for (let i = 0; i < magazine.length; i++){
        const currChar = magazine[i];
        if (magHash[currChar]) {
            magHash[currChar] += 1;
        } else {
            magHash[currChar] = 1;
        }
    }

    for (let i = 0; i < ransomNote.length; i++) {
        const currChar = ransomNote[i];

        if (!magHash[currChar] || magHash[currChar] === 0) {
            return false;
        } else {
            magHash[currChar] = magHash[currChar] - 1;
        }
    }
    return true;
}; 