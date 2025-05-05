impl Solution {
    pub fn num_tilings(n: i32) -> i32 {
        if n<=2{
            return n;
        }
        let n=n as usize;
        let modulo=10_i64.pow(9)+7;
        let mut dp=vec![[0,0,0];n+1];
        dp[0][0]=1;
        dp[1][0]=1;
        for i in 2..=n{
            dp[i][0]=(dp[i-1][0]+dp[i-2][0]+dp[i-1][1]+dp[i-1][2])%modulo;
            dp[i][1]=(dp[i-2][0]+dp[i-1][2])%modulo;
            dp[i][2]=(dp[i-2][0]+dp[i-1][1])%modulo;
        }
        dp[n][0] as i32
    }
}

//QED   
//Problem 790 - (Medium of Domino And Tromino Tiling) - Jason Balayev (rust)
