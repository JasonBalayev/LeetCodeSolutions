impl Solution {
    pub fn triangle_type(nums: Vec<i32>) -> String {
        let mut sides=nums.clone();
        sides.sort();
        if sides[0]+sides[1]<=sides[2]{
            return "none".to_string();
        }
        if sides[0]==sides[1]&&sides[1]==sides[2]{
            return "equilateral".to_string();
        }else if sides[0]==sides[1]||sides[1]==sides[2]||sides[0]==sides[2]{
            return "isosceles".to_string();
        }else{
            return "scalene".to_string();
        }
    }
}

//QED
//Problem 3024 (Easy of Type Of Triangle) - Jason Balayev (rust)