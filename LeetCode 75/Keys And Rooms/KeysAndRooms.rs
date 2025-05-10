use std::collections::HashSet;
impl Solution {
    pub fn can_visit_all_rooms(rooms: Vec<Vec<i32>>) -> bool {
        let n=rooms.len();
        let mut visited=HashSet::new();
        Self::dfs(0,&rooms,&mut visited);
        visited.len()==n   
    }
    fn dfs(room:usize,rooms:&Vec<Vec<i32>>,visited:&mut HashSet<usize>){
        visited.insert(room);
        for &key in &rooms[room]{
            let next_room=key as usize;
            if !visited.contains(&next_room){
                Self::dfs(next_room,rooms,visited)
            }
        }
    }
}

//QED
//Problem 841 (Medium of Keys And Rooms) - Jason Balayev (rust)