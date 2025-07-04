impl Solution {
    pub fn kth_character(k: i64, operations: Vec<i32>) -> char {
        let mut len:u128=1;
        for _ in &operations{
            len*=2;
        }
        let mut pos:u128=(k as u128)-1;
        let mut shift:u32=0;
        for &op in operations.iter().rev(){
            len/=2;
            if pos>=len{
                pos-=len;
                if op==1{
                    shift=(shift+1)%26;
                }
            }
        }
        let ch_byte=b'a'+(shift as u8);
        ch_byte as char
    }
} 

//QED
//Problem 3307 (Hard of Find The K-th Character In String Game II) - Jason Balayev (rs)