impl Solution {
    pub fn color_the_grid(m: i32, n: i32) -> i32 {
        const Mod:i32=1_000_000_007;
        let m=m as usize;
        let n=n as usize;
        let total_states = 3usize.pow(m as u32);
        let mut valid_states=Vec::new();
        let mut color=vec![vec![0; m];total_states];
        let mut dp=vec![vec![0; total_states];n+1];
        let mut is_valid=vec![vec![0;total_states];total_states];
        for i in 0..total_states{
            let mut val=i;
            let mut is_ok=true;
            for j in 0..m{
                color[i][j]=val%3;
                val/=3;
            }
            for j in 1..m{
                if color[i][j]==color[i][j-1]{
                    is_ok=false;
                    break;
                }
            }
            if is_ok{
                valid_states.push(i);
                dp[1][i]=1;
            }
        }
        for &i in &valid_states{
            for &j in &valid_states{
                is_valid[i][j]=1;
                for k in 0..m{
                    if color[i][k]==color[j][k]{
                        is_valid[i][j]=0;
                        break;
                    }
                }
            }
        }
        for col in 2..=n{
            for &i in &valid_states{
                for &j in &valid_states{
                    if is_valid[i][j]==1{
                        dp[col][i]=(dp[col][i]+dp[col-1][j])%Mod;
                    }
                }
            }
        }        
        let mut res=0;
        for &i in &valid_states{
            res=(res+dp[n][i])%Mod;
        }
        res
    }
}

//QED
//Problem 1931 (Hard of Painting A Grid With Three Different Colors) - Jason Balayev (rust)