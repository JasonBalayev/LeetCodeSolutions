impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        if nums.is_empty(){
            return vec![];
        }
        let mut res=Vec::new();
        let mut start=nums[0];
        let mut end=nums[0];
        for i in 1..nums.len(){
            if nums[i]==end+1{
                end=nums[i];
            }else{
                if start==end{
                    res.push(start.to_string());
                }else{
                    res.push(format!("{}->{}",start,end));
                }
                start=nums[i]
                end=nums[i]
            }
        }
        if start==end{
            res.push(start.to_string());
        }else{
            res.push(format!("{}->{}",start,end));
        }
        res
    }
}

//QED
//Problem 228 (Medium of Zero Array Transformation III) - Jason Balayev (rust)