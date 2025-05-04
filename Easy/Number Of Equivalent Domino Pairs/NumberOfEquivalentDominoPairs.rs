use std::collections::HashMap;
impl Solution {
    pub fn num_equiv_domino_pairs(dominoes: Vec<Vec<i32>>) -> i32 {
        let mut count_map:HashMap<(i32,i32),i32>=HashMap::new();
        let mut pairs=0;
        for domino in dominoes{
            let key=if domino[0]<=domino[1]{
                (domino[0],domino[1])
            }else{
            (domino[1],domino[0])
        };
        let count=count_map.entry(key).or_insert(0);
        pairs+=*count;
        *count+=1;
        }
        pairs
    }
}

//QED
//Problem 1128 (Easy of Number Of Equivalent Domino Pairs) - Jason Balayev (rust)