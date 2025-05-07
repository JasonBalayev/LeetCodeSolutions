use std::collections::BinaryHeap;
use std::cmp::Reverse;
impl Solution {
    pub fn min_time_to_reach(move_time: Vec<Vec<i32>>) -> i32 {
        let rows=move_time.len();
        let cols=move_time[0].len();
        let mut dist=vec![vec![i32::MAX;cols];rows];
        dist[0][0]=0;
        let mut pq=BinaryHeap::new();
        pq.push(Reverse((0,0,0)));
        let dirs=[(0,1),(1,0),(0,-1),(-1,0)];
        while let Some(Reverse((time,r,c)))=pq.pop(){
            if r==rows-1&&c==cols-1{
                return time;
            }
            if time>dist[r][c]{
                continue;
            }
            for (dr,dc) in &dirs{
                let nr=r as i32+dr;
                let nc=c as i32+dc;
                if nr>=0&&nr<rows as i32&&nc>=0&&nc<cols as i32{
                    let nr=nr as usize;
                    let nc=nc as usize;
                    let start_time=std::cmp::max(time,move_time[nr][nc]);
                    let arrival=start_time+1;
                    if arrival<dist[nr][nc]{
                        dist[nr][nc]=arrival;
                        pq.push(Reverse((arrival,nr,nc)));
                    }
                }
            }
        }
        -1
    }
}

//QED
//Problem 3341 - (Medium of Find Minimum Time To Reach Last Room I) - Jason Balayev (rust)