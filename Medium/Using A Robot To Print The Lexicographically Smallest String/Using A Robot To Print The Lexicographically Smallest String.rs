impl Solution {
    pub fn robot_with_string(s: String) -> String {
        let s_bytes=s.as_bytes();
        let len=s_bytes.len();
        let mut min_suffix=vec![b'z'+1;len+1];
        for i in (0..len).rev(){
            min_suffix[i]=min_suffix[i+1].min(s_bytes[i]);
        }
        let mut t:Vec<u8>=Vec::with_capacity(len);
        let mut paper:Vec<u8>=Vec::with_capacity(len);
        for i in 0..len{
            t.push(s_bytes[i]);
            while let Some(&top)=t.last(){
                if top<=min_suffix[i+1]{
                    paper.push(t.pop().unwrap());
                }else{
                    break;
                }
            }
        }
        while let Some(ch)=t.pop(){
            paper.push(ch);
        }
        unsafe{String::from_utf8_unchecked(paper)}
    }
}

//QED
//Problem 2434 (Medium of Using A Robot To Print The Lexicographically Smallest String) - Jason Balayev (rust)