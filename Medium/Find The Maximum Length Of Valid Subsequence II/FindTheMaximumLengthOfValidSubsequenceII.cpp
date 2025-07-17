class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        int n=nums.size();
        if (n==0)return 0;
        vector<vector<int>>dp(k,vector<int>(k,0));
        vector<int>len1(k,0);
        int ans=1; 
        for (int val:nums) {
            int mod=val%k;
            vector<int>new_len(k, 0);
            for (int r=0;r<k;++r) {
                int prev_mod=(r-mod+k)%k;
                int prev_len=dp[r][prev_mod];
                if (len1[prev_mod]){
                    prev_len=max(prev_len,1);
                }
                if(prev_len){
                    new_len[r]=prev_len+1;
                    ans=max(ans,new_len[r]);
                }
            }
            for(int r=0;r<k;++r){
                dp[r][mod]=max(dp[r][mod],new_len[r]);
            }
            len1[mod]=1;
        }
        return ans;
    }
};

//QED
//Problem 3202 (Medium Of Find The Maximum Length Of Valid Subsequence II) - Jason Balayev (cpp)
