class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        vector<int>sorted=nums;
        sort(sorted.begin(),sorted.end(),greater<int>());
        unordered_map<int,int>need;
        for(int i=0;i<k;++i)need[sorted[i]]++;
        vector<int>ans;
        for(int x:nums){
            if(need[x]>0){
                ans.push_back(x);
                --need[x];
                if(ans.size()==k)break;
            }
        }
        return ans;
    }
};

//QED
//Problem 2099 (Easy of Find Subsequence Of Length K With The Largest Sum) - Jason Balayev (cpp)