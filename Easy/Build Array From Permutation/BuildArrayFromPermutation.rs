impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut res=vec![0;nums.len()];
        for i in 0..nums.len(){
            let idx=nums[i] as usize;
            res[i]=nums[idx];
        }
        res
    }
}

//QED
//Problem 1920 - (Easy of Build Array From Permutation) - Jason Balayev (rust)