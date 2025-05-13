impl Solution {
    pub fn length_after_transformations(s: String, t: i32) -> i32 {
        const modulo:i64=1_000_000_007;
        let mut count=[0i64;26];
        for c in s.chars(){
            count[(c as u8-b'a')as usize]+=1;
        }
        for i in 0..t{
            let mut new_count=[0i64;26];
            new_count[0]+=count[25];
            new_count[1]+=count[25];
            for i in 0..25{
                new_count[i+1]+=count[i];
            }
            for i in 0..26{
                count[i]=new_count[i]%modulo;
            }  
        }
        let total:i64=count.iter().sum::<i64>()%modulo;
        total as i32
    }
}

//QED
//Problem 3335 (Medium ofTotal Characters In String After Transformations I) - Jason Balayev (rust)