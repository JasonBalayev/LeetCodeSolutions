class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        vector<long long> dp(n,0);
        dp[n-1] = questions[n-1][0];

        for (int i=n-2; i>=0; --i) {
            long long take = questions[i][0];
            int next = i+questions[i][1] + 1;
            if (next<n) {
                take += dp[next];
            }
            long long skip = dp[i+1];
            dp[i] = max(take,skip);
        }
        return dp[0];
    }
};

//QED
//Problem 2140 (Medium of Solving Questions With Brainpower) - Jason Balayev (cpp)