impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut count=0;
        let mut element=0;
        for num in nums{
            if count==0{
                element=nums;
            }
            count+=if num==element{1}else{-1};
        }
        element
    }
}

//QED
//Problem 169 (Easy of Majority Element - Jason Balayev (rust)