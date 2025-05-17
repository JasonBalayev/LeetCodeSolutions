impl Solution {
    pub fn hammingWeight(n: u32) -> i32 {
        n.count_ones() as i32
    }
}

//QED
//Problem 191 (Easy of Number of 1 Bits) - Jason Balayev (rust)