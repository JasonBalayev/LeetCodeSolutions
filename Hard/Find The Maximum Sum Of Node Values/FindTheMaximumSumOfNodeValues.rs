impl Solution {
    pub fn maximum_value_sum(nums: Vec<i32>, k: i32, edges: Vec<Vec<i32>>) -> i64 {
        let mut total:i64=0;
        let mut diff:Vec<i64>=Vec::new();
        for &num in &nums{
            let original_val=num as i64;
            let xor=(num^k) as i64;
            total+=original_val;
            diff.push(xor-original_val);
        }
            diff.sort_unstable_by(|a,b|b.cmp(a));
            let mut add:i64=0;
            let mut idx=0;
            while idx+1<diff.len(){
                let pair=diff[idx]+diff[idx+1];
                if pair>0{
                    add+=pair;
                    idx+=2;
                }else{
                    break;
                }
            }
            total+add
        }
}

//QED
//Problem 3068 (Hard of Find The Maximum Sum Of Node Values) - Jason Balayev (rust)