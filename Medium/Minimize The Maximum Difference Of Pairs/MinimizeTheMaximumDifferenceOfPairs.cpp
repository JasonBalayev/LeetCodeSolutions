class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        if(p==0)return 0;
        sort(nums.begin(),nums.end());
        int l=0,r=nums.back()-nums[0];
        while(l<r){
            int m=l+(r-l)/2;
            if(ok(nums,p,m)){
                r=m;
            }else{
                l=m+1;
            }
        }
        return l;
    }   
    bool ok(vector<int>&nums,int p,int x){
        int c=0;
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i+1]-nums[i]<=x){
                c++;
                i++;
                if(c==p)return true;
            }
        }
        return false;
    }
};

//QED
//Problem 2616 (Medium of Minimize The Maximum Difference Of Pairs) - Jason Balayev (cpp)