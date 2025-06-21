class Solution {
public:
    int addDigits(int num) {
        while(num>9){
            int sum=0;
            while(num>0){
                sum+=num%10;
                num/=10;
            }
            num=sum;
        }
        return num;
    }
};

//QED
//Problem 258 (Easy of Add Digits) - Jason Balayev (cpp)