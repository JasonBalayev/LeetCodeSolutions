use std::collections::HashMap;
impl Solution {
    pub fn count_balanced_permutations(num: String) -> i32 {
        let digits: Vec<i32> = num.chars().map(|c| c.to_digit(10).unwrap() as i32).collect();
        let mut digitFreq=HashMap::new();
        for &d in &digits {
            *digitFreq.entry(d).or_insert(0)+=1;
        }
        let totalSum:i32=digits.iter().sum();
        if totalSum%2!=0{
            return 0;
        }
        let targetSum=totalSum/2;
        let firstHalfSize=digits.len()/2;
        let secondHalfSize=(digits.len()+1)/2;
        let modulo=1_000_000_007;
        let mut comboMemo=HashMap::new();
        let mut permMemo=HashMap::new();
        fn choose(n:usize,k:usize,modulo:i32,memo:&mut HashMap<(usize,usize),i32>)->i32 {
            if k==0||n== 0||n==k{
                return 1;
            }
            if let Some(&res)=memo.get(&(n,k)){
                return res;
            }
            let res=(choose(n-1,k-1,modulo, memo)+choose(n-1,k,modulo,memo))%modulo;
            memo.insert((n,k),res);
            return res;
        }
        fn permutations(
            currentDigit:i32, 
            remainingSum:i32, 
            firstHalfRemaining:usize, 
            secondHalfRemaining:usize, 
            digitFreq:&HashMap<i32,i32>,
            modulo:i32,
            comboMemo:&mut HashMap<(usize,usize),i32>,
            permMemo:&mut HashMap<(i32,i32,usize,usize),i32>
        )->i32{
            if remainingSum==0&&firstHalfRemaining==0&&secondHalfRemaining==0{
                return 1;
            }
            if(remainingSum<0)||(remainingSum>0&&firstHalfRemaining==0)||(remainingSum>0&&currentDigit>9)||((firstHalfRemaining as i32)<0)||((secondHalfRemaining as i32)<0){
                return 0;
            }
            if let Some(&res)=permMemo.get(&(currentDigit,remainingSum,firstHalfRemaining,secondHalfRemaining)){
                return res;
            }
            let mut totalWays=0;
            let digitCount=*digitFreq.get(&currentDigit).unwrap_or(&0);
            for firstHalfCount in 0..=std::cmp::min(firstHalfRemaining, digitCount as usize){
                let secondHalfCount=digitCount as usize-firstHalfCount;
                if secondHalfCount<=secondHalfRemaining{
                    let subResult=permutations(
                        currentDigit+1, 
                        remainingSum-(firstHalfCount as i32*currentDigit), 
                        firstHalfRemaining-firstHalfCount, 
                        secondHalfRemaining-secondHalfCount,
                        digitFreq,
                        modulo,
                        comboMemo,
                        permMemo
                    );
                    let firstHalfWays = choose(firstHalfRemaining,firstHalfCount,modulo,comboMemo);
                    let secondHalfWays=choose(secondHalfRemaining,secondHalfCount,modulo,comboMemo);
                    
                    let newWays = (((subResult as i64*firstHalfWays as i64)%modulo as i64) 
                                   *secondHalfWays as i64)%modulo as i64;
                    
                    totalWays=(totalWays+newWays as i32)%modulo;
                }
            }
            permMemo.insert((currentDigit,remainingSum,firstHalfRemaining,secondHalfRemaining),totalWays);
            totalWays
        }
        permutations(0,targetSum,firstHalfSize,secondHalfSize,&digitFreq,modulo,&mut comboMemo,&mut permMemo)
    }
}
 
//QED
//Problem 3343 (Hard of Count Number Of Balanced Permutations) - Jason Balayev (rust)
//Referenced wanderingCicada's sol