impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let n=cost.len();
        let mut prev1=0;
        let mut prev2=0;
        for i in 2..=n{
            let curr=std::cmp::min(
                prev1+cost[i-2],
                prev2+cost[i-1]
            );
            prev1=prev2;
            prev2=curr;
        }
        prev2
    }
}

//QED
//Problem 746 (Easy of Min Cost Climbing Stairs) - Jason Balayev (rust)