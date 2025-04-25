class Solution {
public:
    long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
        int n=nums.size();
        long long count=0;
        vector<int> transformed(n);
        for (int i=0; i<n; i++){
            transformed[i]=(nums[i]%modulo==k) ? 1:0;
        }
        vector<int> prefix(n+1,0);
        for (int i=0; i<n; i++){
            prefix[i+1]=(prefix[i]+transformed[i]) % modulo;
        }
        unordered_map<int,int> prefixCount;
        prefixCount[0]=1;
        for (int i=1; i<=n; i++){
            int remainder=(prefix[i]-k+modulo) % modulo;
            count+=prefixCount[remainder];
            prefixCount[prefix[i]]++;
        }
        return count;
    }
};

//QED
//Problem 2825 (Medium of Count Of Interesting Subarrays) - Jason Balayev (cpp)