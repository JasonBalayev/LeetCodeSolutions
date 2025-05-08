impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        if n==0{return 0;}
        if n==1||n==2  {return 1;}
        let mut t0=0;
        let mut t1=1;
        let mut t2=1;
        for i in 3..=n{
            let next=t0+t1+t2;
            t0=t1;
            t1=t2;
            t2=next;
        }
        t2
    }
}

//QED
//Problem 1137 (Easy of N-th Tribonacci Number) - Jason Balayev (rust)