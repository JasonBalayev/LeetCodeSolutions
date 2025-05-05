use std::collections::VecDeque;
impl Solution {
    pub fn predict_party_victory(senate: String) -> String {
        let n=senate.len();
        let mut radiant=VecDeque::new();
        let mut dire=VecDeque::new();
        for (i,c) in senate.chars().enumerate(){
            if c=='R'{
                radiant.push_back(i);
            }else{
                dire.push_back(i);
            }
        }
        while !radiant.is_empty()&&!dire.is_empty(){
            let r_idx=radiant.pop_front().unwrap();
            let d_idx=dire.pop_front().unwrap();
            if r_idx<d_idx{
                radiant.push_back(r_idx+n);
            }else{
                dire.push_back(d_idx+n);
            }
        }
        if radiant.is_empty(){
            return "Dire".to_string();
        }else if dire.is_empty(){
            return "Radiant".to_string();
        }
        unreachable!()
    }
}

//QED
//Problem 649 - (Medium of Dota2 Senate) - Jason Balayev (rust)