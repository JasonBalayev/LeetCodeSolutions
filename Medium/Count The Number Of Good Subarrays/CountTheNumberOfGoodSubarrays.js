/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countGood = function(nums, k) {
    const n=nums.length;
    let res= 0;
    let pair=0;
    let left=0;
    const freq = new Map();

    for (let right=0; right<n; right++) {
        const currNum = nums[right];
        const currFreq = freq.get(currNum)||0;
        pair+=currFreq;
        freq.set(currNum,currFreq+1);

        while (pair>=k) {
            res+=n-right;
            const leftNum=nums[left];
            const leftFreq=freq.get(leftNum);
            pair-=(leftFreq-1);
            freq.set(leftNum,leftFreq-1);
            left++;
        }
    }
    return res
};

//QED
//Problem 2537 (Medium of Count The Number Of Good Subarrays) - Jason Balayev (js)