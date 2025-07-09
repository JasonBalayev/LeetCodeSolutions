class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        sort(events.begin(),events.end());        
        int n=events.size();
        vector<vector<int>>dp(n+1,vector<int>(k+1,0));
        for (int i=n-1;i>=0;--i){
            auto it=upper_bound(events.begin()+i+1,events.end(),events[i][1],[](int end_day,const vector<int>& event){
                return end_day<event[0];
            });
            int next_event=distance(events.begin(),it);
            for (int j=1;j<=k;++j){
                int skip=dp[i+1][j];
                int attend=events[i][2]+dp[next_event][j-1];
                dp[i][j]=max(skip,attend);
            }
        }
        return dp[0][k];
    }
};

//QED
//Problem 1751 (Hard of Maximum Number of Events That Can Be Attended II) - Jason Balayev (cpp)