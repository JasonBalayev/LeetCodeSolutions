function countGood(nums: number[], k: number): number {
    const n=nums.length;
    let res=0;
    let pair=0;
    let left=0;
    const freq=new Map<number,number>();

    for (let right=0; right<n; right++) {
        const currNum=nums[right];
        const currFreq=freq.get(currNum)||0;
        pair+=currFreq;
        freq.set(currNum,currFreq+1);

        while (pair>=k) {
            res+=n-right;
            const leftNum=nums[left];
            const leftFreq=freq.get(leftNum)||0;
            pair-=(leftFreq-1);
            freq.set(leftNum,leftFreq-1);
            left++;
        }
    }
    
    return res;
}

//QED
//Problem 2537 (Medium of Count The Number Of Good Subarrays) - Jason Balayev (ts)