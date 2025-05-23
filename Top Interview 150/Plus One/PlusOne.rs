impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut res=digits.clone();
        let n=res.len();
        for i in (0..n).rev(){
            if res[i]<9{
                res[i]+=1;
                return res;
            }
            res[i]=0;
        }
        let mut new_res=vec![1];
        new_res.extend(res);
        new_res
    }
}

//QED
//Problem 66 (Easy of Plus One) - Jason Balayev (rust)