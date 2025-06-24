class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        int n=nums.size();
        vector<int> keyIndices;
        for(int i=0;i<n;i++){
            if(nums[i]==key)keyIndices.push_back(i);
        }
        vector<bool>marked(n,false);
        for(int idx:keyIndices){
            int l=max(0,idx-k);
            int r=min(n-1,idx+k);
            for(int i=l;i<=r;++i){
                marked[i]=true;
            }
        }
        vector<int>res;
        for(int i=0;i<n;i++){
            if(marked[i])res.push_back(i);
        }
        return res;
    }
};

//QED
//Problem 2200 (Hard of Find All K-Distant Indices In An Array) - Jason Balayev (cpp)