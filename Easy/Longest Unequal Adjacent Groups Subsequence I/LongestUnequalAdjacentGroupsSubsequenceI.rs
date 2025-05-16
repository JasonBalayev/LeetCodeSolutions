impl Solution {
    pub fn get_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let mut res=Vec::new();
        if !words.is_empty(){
            res.push(words[0].clone());
        }
        let mut last=if !groups.is_empty(){groups[0]}else{-1};;
        for i in 1..words.len(){
            if groups[i]!=last{
                res.push(words[i].clone());
                last=groups[i]
            }
        }
        res
    }
}

//QED
//Problem 2900 (Easy of Longest Unequal Adjacent Groups Subsequence I) - Jason Balayev (rust)