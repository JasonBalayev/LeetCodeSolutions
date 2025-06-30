class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int,int>freq;
        for(int num:nums){
            ++freq[num];
        }
        int longest=0;
        for(const auto&[val,count]:freq){
            auto it=freq.find(val+1);
            if(it!=freq.end()){
                longest=max(longest,count+it->second);
            }
        }
        return longest;
    }
};

//QED
//Problem 594 (Easy of Longest Harmonious Subsequence) - Jason Balayev (cpp)