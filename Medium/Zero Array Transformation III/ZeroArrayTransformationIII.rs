use std::collections::BinaryHeap;
impl Solution {
    pub fn max_removal(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let mut queries = queries.clone();
        queries.sort_by_key(|x|x[0]);
        let mut available=BinaryHeap::new();
        let mut assigned=BinaryHeap::new();
        let mut count=0;
        let mut k=0;
        for time in 0..nums.len(){
            while !assigned.is_empty()&&-assigned.peek().unwrap()<time as i32{
                assigned.pop();
            }
            while k<queries.len()&&queries[k][0]<=time as i32{
                available.push(queries[k][1]);
                k+=1;
            }
            while assigned.len()<nums[time] as usize&&!available.is_empty()&&*available.peek().unwrap()>=time as i32{
                assigned.push(-available.pop().unwrap());
                count += 1;
            }
            if assigned.len()<nums[time] as usize{
                return -1;
            }
        }
        (queries.len() as i32)-count
    }
} 

//QED
//Problem 3362 (Medium of Zero Array Transformation III) - Jason Balayev (rust)