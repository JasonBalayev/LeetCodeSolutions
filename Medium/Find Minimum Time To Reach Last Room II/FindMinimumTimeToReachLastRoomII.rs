use std::collections::BinaryHeap;
use std::cmp::Reverse;
impl Solution {
    pub fn min_time_to_reach(move_time: Vec<Vec<i32>>) -> i32 {
        let(rows,cols)=(move_time.len(),move_time[0].len());
        let mut dist=vec![vec![i32::MAX;cols];rows];
        dist[0][0]=0;
        let mut pq=BinaryHeap::new();
        pq.push(Reverse((0,0,0,1)));
        let dirs=[(0,1),(1,0),(0,-1),(-1,0)];
        while let Some(Reverse((time,r,c,cost)))=pq.pop(){
            if r==rows-1&&c==cols-1{
                return time;
            }
            if time>dist[r][c]{
                continue;
            }
            for(dr,dc) in &dirs{
                let nr=r as i32+dr;
                let nc=c as i32+dc;
                if nr>=0&&nr<rows as i32&&nc>=0&&nc<cols as i32{
                    let(nr,nc)=(nr as usize, nc as usize);
                    let start=time.max(move_time[nr][nc]);
                    let next_time=start+cost;
                    let next_cost=if cost==1{2}else{1};
                    if next_time<dist[nr][nc]{
                        dist[nr][nc]=next_time;
                        pq.push(Reverse((next_time,nr,nc,next_cost)));
                    }
                }
            }
        }
        -1
    }
}

//QED
//Problem 3342 (Medium of Find Minimum Time To Reach Last Room II) - Jason Balayev (rust)
