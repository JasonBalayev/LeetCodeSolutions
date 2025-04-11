class Solution {
public:
    int countSymmetricIntegers(int low, int high) {
        int count =0;

        for (int num = low; num<= high; num++) {
            string numString = to_string(num);
            int len = numString.length();
            
            if (len%2 != 0) continue;
            int firstSum = 0;
            int secondSum = 0;

            for (int i = 0; i<len/2; i++) {
                firstSum += numString[i] -'0';
                secondSum += numString[i+len/2] - '0';
            }
            if (firstSum == secondSum) {
                count++;
            }
        }
        return count++;
        
    }
};

//QED
//Problem 2843 (Easy of Count Symmetric Integers) - Jason Balayev (cpp)