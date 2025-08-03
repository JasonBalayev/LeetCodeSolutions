class Solution {
    public:
        int maxTotalFruits(vector<vector<int>>& fruits, int startPos, int k) {
            int n=fruits.size();
            int l=0;
            int sum=0;
            int maxSum=0;
            for(int r=0;r<n;r++){
                sum+=fruits[r][1];
                while(l<=r&&getSteps(fruits[l][0],fruits[r][0],startPos)>k){
                    sum-=fruits[l][1];
                    l++;
                }            
                maxSum=max(maxSum,sum);
            }        
            return maxSum;
        }
    private:
        int getSteps(int lPos,int rPos,int st){
            int leftFirst=abs(st-lPos)+(rPos-lPos);
            int rightFirst=abs(st-rPos)+(rPos-lPos);
            return min(leftFirst, rightFirst);
        }
    };

//QED
//Problem 2106 (Hard of Maximum Fruits Harvested After At Most K Steps) - Jason Balayev (cpp)