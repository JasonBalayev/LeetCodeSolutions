impl Solution {
    pub fn find_even_numbers(digits: Vec<i32>) -> Vec<i32> {
        let mut elements=[0;10];
        for &digit in &digits{
            elements[digit as usize]+=1;
        }
        let mut res=Vec::new();
        for num in 100..1000{
            if num%2!=0{
                continue;
            }
            let hundreds=num/100;
            let tens=(num/10)%10;
            let ones=num%10;
            let mut copy=elements.clone();
            copy[hundreds as usize]-=1;
            if copy[hundreds as usize]<0{
                continue;
            }
            copy[tens as usize]-=1;
            if copy[tens as usize]<0{
                continue;
            }
            copy[ones as usize]-=1;
            if copy[ones as usize]<0{
                continue;
            }
            res.push(num);
        }
        res
    }
}

//QED
//Problem 2094 (Easy of Finding 3-Digits Even Numbers) - Jason Balayev (rust)