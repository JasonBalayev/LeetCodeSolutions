impl Solution {
    pub fn three_consecutive_odds(arr: Vec<i32>) -> bool {
        if arr.len()<3{
            return false;
        }
        for i in 0..arr.len()-2{
            if arr[i]&1==1&&arr[i+1]&1==1&&arr[i+2]&1==1{
                return true;
            }
        }
        false
    }
}

//QED
//Problem 1550 (Easy of Three Consecutive Odds) - Jason Balayev (rust)