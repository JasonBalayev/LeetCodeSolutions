impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n<=2{
            return n;
        }
        let mut prev=1;
        let mut curr=2;
        for i in 3..=n{
            let next=prev+curr;
            prev=curr;
            curr=next;
        }
        curr
    }
}

//QED
//Problem 70 (Easy of Climbing Stairs) - Jason Balayev (rust)