impl Solution {
    pub fn answer_string(word: String, num_friends: i32) -> String {
        if num_friends==1{
            return word;
        }
        let chars:Vec<char>=word.chars().collect();
        let n=chars.len();
        let seg_len=n as i32-num_friends+1;
        let mut best=String::new();
        for start in 0..n{
            let end=((start as i32)+seg_len).min(n as i32) as usize;
            let candid:String=chars[start..end].iter().collect();
            if candid>best{
                best=candid;
            }
        }
        best
    }
}

//QED
//Problem 3403 (Medium of Find The Lexicographically Largest String From The Box I) - Jason Balayev (rust)    