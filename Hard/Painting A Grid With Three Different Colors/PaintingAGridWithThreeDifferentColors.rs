impl Solution {
    pub fn color_the_grid(m: i32, n: i32) -> i32 {
        let m=m as usize;
        let n=n as usize;
        const Mod:i32=1_000_000_007;
        if m==1{
            let mut res:i64=3;
            for i in 1..n{
                res=(res*2)%(Mod as i64);
            }
            return res as i32;
        }
        if m==2{
            if n==1{
                return 6;
            }
            if n==2 {
                return 18;
            }
            let mut a:i64=6;
            let mut b:i64=6;
            for i in 1..n{
                let new_a=(3*a+2*b)%(Mod as i64);
                let new_b=(2*a+2*b)%(Mod as i64);
                a=new_a;
                b=new_b;
            }
            return a as i32;
        }
        let mut states=Vec::new();
        let mut map=std::collections::HashMap::new();
        fn gen_states(row:usize,m:usize,curr:Vec<u8>,states:&mut Vec<Vec<u8>>){
            if row==m{
                states.push(curr);
                return;
            }
            for color in 1..=3{
                if row>0&&curr[row-1]==color{
                    continue;
                }
                let mut new_curr=curr.clone();
                new_curr.push(color);
                gen_states(row+1,m,new_curr,states);
            }
        }
        
        gen_states(0,m,Vec::new(),&mut states);
        
        for (i,state) in states.iter().enumerate(){
            map.insert(state.clone(),i);
        }
        let count=states.len();
        let mut adj=vec![Vec::new();count];
        for i in 0..count{
            for j in 0..count{
                let mut valid=true;
                for k in 0..m{
                    if states[i][k]==states[j][k]{
                        valid=false;
                        break;
                    }
                }
                if valid{
                    adj[i].push(j);
                }
            }
        }
        let mut dp=vec![1i64;count];
        for _ in 1..n{
            let mut new_dp=vec![0i64;count];
            for i in 0..count{
                for &j in &adj[i]{
                    new_dp[j]=(new_dp[j]+dp[i])%(Mod as i64);
                }
            }
            dp=new_dp;
        }
        (dp.iter().sum::<i64>()%(Mod as i64)) as i32
    }
}

//QED
//Problem 1931 (Hard of Painting A Grid With Three Different Colors) - Jason Balayev (rust)