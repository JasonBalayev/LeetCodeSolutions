impl Solution {
    pub fn is_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> bool {
        let mut op=vec![0;nums.len()+1];
        for query in &queries{
            let start=query[0] as usize;
            let end=query[1] as usize;
            op[start]+=1;
            if end+1<nums.len(){
                op[end+1]-=1;
            }
        }
        let mut total=0;
        for i in 0..nums.len(){
            total+=op[i];
            if nums[i]>total{
                return false;
            }
        }
        true
    }
}

//QED
//Problem 3355 (Medium of Zero Array Transformation I - Jason Balayev (rust)
