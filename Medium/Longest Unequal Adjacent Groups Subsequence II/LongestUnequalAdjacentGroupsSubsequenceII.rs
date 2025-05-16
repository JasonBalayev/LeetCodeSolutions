impl Solution {
    pub fn get_words_in_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let n=words.len();
        fn hamming_distance(word1:&str,word2:&str)->bool{
            if word1.len()!=word2.len(){
                return false;
            }
            let mut diff=0;
            for(c1,c2) in word1.chars().zip(word2.chars()){
                if c1 != c2{
                    diff+=1;
                    if diff>1{
                        return false;
                    }
                }
            }
            diff==1
        }
        let mut dp=vec![1;n];
        let mut prev=vec![None;n];
        for i in 1..n{
            for j in 0..i{
                if groups[i]!=groups[j]&&hamming_distance(&words[i],&words[j]){
                    if dp[j]+1>dp[i]{
                        dp[i]=dp[j]+1;
                        prev[i]=Some(j);
                    }
                }
            }
        }
        let mut max_len=0;
        let mut end_idx=0;
        for i in 0..n{
            if dp[i]>max_len{
                max_len=dp[i];
                end_idx=i;
            }
        }
        let mut res=Vec::new();
        let mut curr=Some(end_idx);
        while let Some(idx)=curr{
            res.push(words[idx].clone());
            curr=prev[idx];
        }
        res.reverse();
        res
    }
}

//QED
//Problem 2901 (Medium of Longest Unequal Adjacent Groups Subsequence II) - Jason Balayev (rust)