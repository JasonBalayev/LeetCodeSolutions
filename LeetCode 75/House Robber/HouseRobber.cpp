class Solution {
public:
    int rob(vector<int>& nums) {
        int a=0,b=0;
        for(int x:nums){
            int t=a+x>b?a+x:b;
            a=b;
            b=t;
        }
        return b;
    }
};

//QED
//Problem 198 (Medium of House Robber) - Jason Balayev (cpp)