impl Solution {
    pub fn count_bits(n: i32) -> Vec<i32> {
        let mut res=vec![0; n as usize+1];
        for i in 0..=n{
            res[i as usize]=i.count_ones() as i32;
        }
        res
    }
}

//QED
//Problem 338 (Medium of Counting Bits) - Jason Balayev (rust)