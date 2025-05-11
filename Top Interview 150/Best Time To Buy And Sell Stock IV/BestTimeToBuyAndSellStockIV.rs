impl Solution {
    pub fn max_profit(k: i32, prices: Vec<i32>) -> i32 {
        let n=prices.len();
        let k=k as usize;
        if n<2||k==0{
            return 0;
        }
        if k>=n/2{
            let mut maximum_profit=0;
            for i in 1..n{
                if prices[i]>prices[i-1]{
                    maximum_profit+=prices[i]-prices[i-1];
                }
            }
            return maximum_profit;
        }
        let mut dp=vec![vec![0,std::i32::MIN];k+1];
        for price in prices{
            for j in 1..=k{
                dp[j][0]=dp[j][0].max(dp[j][1]+price);
                dp[j][1]=dp[j][1].max(dp[j-1][0]-price);
            }
        }
        dp[k][0]
    }
}

//QED
//Problem 188 (Hard of Best Time to Buy and Sell Stock IV) - Jason Balayev (rust)