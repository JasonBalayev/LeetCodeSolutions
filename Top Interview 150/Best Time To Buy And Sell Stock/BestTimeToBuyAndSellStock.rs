impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        if prices.len()<2{
            return 0;
        }
        let mut min_price=prices[0];
        let mut max_profit=0;
        for price in prices.iter(){
            min_price=min_price.min(*price);
            let curr_profit=price-min_price;
            max_profit=max_profit.max(curr_profit);
        }
        max_profit
    }
}

//QED
//Problem 121 (Easy of Best Time to Buy and Sell Stock) - Jason Balayev (rust)