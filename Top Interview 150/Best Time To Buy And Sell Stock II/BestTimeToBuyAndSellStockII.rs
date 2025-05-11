impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.len()<2{
            return 0;
        }
        let mut maximum_profit=0;
        for i in 1..prices.len(){
            let profit=prices[i]-prices[i-1];
            if profit>0{
                maximum_profit+=profit;
            }
        }
        maximum_profit
    }
}

//QED
//Problem 122 (Medium of Best Time to Buy and Sell Stock II) - Jason Balayev (rust)