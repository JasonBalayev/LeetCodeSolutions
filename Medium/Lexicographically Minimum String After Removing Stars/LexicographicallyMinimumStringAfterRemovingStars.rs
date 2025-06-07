impl Solution {
    pub fn clear_stars(s: String) -> String {
        let chars:Vec<char>=s.chars().collect();
        let n=chars.len();
        let mut buckets:Vec<Vec<usize>>=vec![Vec::new();26];
        let mut removed=vec![false;n];
        for (idx,&ch) in chars.iter().enumerate(){
            if ch=='*'{
                for b in 0..26{
                    if let Some(pos)=buckets[b].pop(){
                        removed[pos]=true;
                        break;
                    }
                }
            }else{
                let bucket_idx=(ch as u8-b'a') as usize;
                buckets[bucket_idx].push(idx);
            }
        }
        let mut res=String::with_capacity(n);
        for (idx,&ch) in chars.iter().enumerate(){
            if ch !='*'&&!removed[idx]{
                res.push(ch);
            }
        }
        res
    }
}

//QED 
//Problem 3170 (Medium of Lexicographically Minimum String After Removing Stars) - Jason Balayev (rust)