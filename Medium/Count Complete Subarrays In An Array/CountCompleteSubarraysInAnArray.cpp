class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        unordered_set<int> distinct;
        for (int num:nums){
            distinct.insert(num);
        } 
        int totalDistinct=distinct.size();
        if (totalDistinct==1){
            int n=nums.size();
            return n*(n+1)/2;
        }
        int count=0;
        int n=nums.size();

        for (int left=0; left<n; left++){
            unordered_map<int,int> elements;
            for (int end=left; end<n; end++){
                elements[nums[end]]++;
                if (elements.size()==totalDistinct){
                    count++;
                }
            }
        }
        return count;
    }
};

//QED
//Problem 2279 (Medium of Count Complete Subarrays In An Array) - Jason Balayev (cpp)  