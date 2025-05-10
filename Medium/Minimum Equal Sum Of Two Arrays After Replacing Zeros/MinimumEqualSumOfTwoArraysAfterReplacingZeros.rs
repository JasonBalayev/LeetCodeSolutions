impl Solution {
    pub fn min_sum(nums1: Vec<i32>, nums2: Vec<i32>) -> i64 {
        let mut zeros1=0;
        let mut zeros2=0;
        let mut sum1:i64=0;
        let mut sum2:i64=0;
        for &num in &nums1{
            if num==0{
                zeros1+=1;
            }
            sum1+=num as i64;
        }
        for &num in &nums2{
            if num==0{
                zeros2+=1;
            }
            sum2+=num as i64;
        }
        let min1=sum1+zeros1 as i64;
        let min2=sum2+zeros2 as i64;
        if zeros1==0&&min1<min2{
            return -1;
        }
        if zeros2==0&&min2<min1{
            return -1;
        }
        std::cmp::max(min1,min2)
    }
}

//QED
//Problem 2918 (Medium of Minimum Equal Sum Of Two Arrays After Replacing Zeros) - Jason Balayev (rust)