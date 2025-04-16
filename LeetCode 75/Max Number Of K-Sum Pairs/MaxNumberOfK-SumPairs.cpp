class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        int op=0;

        for (int num:nums) {
            int c = k-num;
            if (freq[c]>0) {
                op++;
                freq[c]--;
            } else {
                freq[num]++;
            }
        }
        return op;
    }
};



//QED
//Problem 1679 (Medium of Max Number Of K-Sum Pairs) - Jason Balayev (cpp)