//Kadane's algo, Greedy algo, sliding window
// O(n) time 
var maxSubArray = function(nums) {
    let maxSum = nums[0];
    let currentSum = maxSum;


    for (let i = 1; i < nums.length; i++) {
        if (nums[i] + currentSum > nums[i]) {
            currentSum += nums[i];
        } else {
            currentSum = nums[i]
        }

        if (currentSum > maxSum) {
            maxSum = currentSum;
        } 
    }

    return maxSum;

};