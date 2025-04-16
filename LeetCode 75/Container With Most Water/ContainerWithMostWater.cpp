class Solution {
public:
    int maxArea(vector<int>& height) {
        int l=0;
        int r=height.size()-1;
        int maxWater=0;

        while(l<r) {
            int width=r-l;
            int h=min(height[l], height[r]);
            maxWater=max(maxWater,width*h);
            if(height[l]<height[r]) {
                l++;
            } else {
            r--;
            }

        }
        return maxWater;
    }
};

//QED
//Problem 11 (Medium of Container With Most Water) - Jason Balayev (cpp)