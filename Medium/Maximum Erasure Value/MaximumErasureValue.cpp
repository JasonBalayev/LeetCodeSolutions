class Solution {
    public:
        int maximumUniqueSubarray(vector<int>& nums) {
            const int max=10000;
            vector<int>freq(max+1,0);
            long long curr=0;
            long long maxSum=0;
            int l=0;
            for(int r=0;r<(int)nums.size();++r){
                int val=nums[r];
                curr+=val;
                freq[val]++;
                while(freq[val]>1){
                    curr-=nums[l];
                    freq[nums[l]]--;
                    ++l;
                }
                if(curr>maxSum){
                    maxSum=curr;
                }
            }
            return(int)maxSum;
        }
    };

    //QED
    //Problem 1695 (Medium Of Maximum Erasure Value) - Jason Balayev (cpp)
