function containsDuplicate(nums: number[]): boolean {
    const set = new Set(nums);
    return set.size !== nums.length;
};

//QED
//Problem 217 (Easy of Contains Duplicate) - Jason Balayev (ts)