class Solution {
    public:
        int maxSum(vector<int>& nums) {
            unordered_set<int>s;
            int n=(int)nums.size();
            int l=0;
            int cur=0,best=INT_MIN;
            for(int r=0;r<n;++r){
                while(s.count(nums[r])){
                    s.erase(nums[l]);
                    cur-=nums[l];
                    ++l;
                }
                s.insert(nums[r]);
                cur+=nums[r];
                if(cur>best)best=cur;
            }
            return best;
        }
    };
