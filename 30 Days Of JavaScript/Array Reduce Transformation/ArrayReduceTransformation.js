/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let val=init;
    for (let i=0; i<nums.length;i++){
        val=fn(val,nums[i]);
    }
    return val;
};

//QED
//Problem 2626 (Easy Of Array Reduce Transformation) - Jason Balayev (javascript)