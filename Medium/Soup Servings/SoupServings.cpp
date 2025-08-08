class Solution {
    public:
        double soupServings(int n) {
            if(n>=5000) return 1.0;
            int size=(n+24)/25;
            vector<vector<double>> memo(size+1,vector<double>(size+1,-1.0));
            return solve(size,size,memo);
        }
    private:
        double solve(int a, int b, vector<vector<double>>&memo){
            if(a<=0&&b<=0) return 0.5;
            if(a<=0) return 1.0;
            if(b<=0) return 0.0;
            if(memo[a][b]!=-1.0){
                return memo[a][b];
            }
            double prob=0.25*solve(max(0,a-4),b,memo)+
                0.25*solve(max(0,a-3),max(0,b-1),memo)+
                0.25*solve(max(0,a-2),max(0,b-2),memo)+
                0.25*solve(max(0,a-1),max(0,b-3),memo);
            memo[a][b]=prob;
            return prob;
        }
};

//QED
//Problem 808 (Medium of Soup Servings) - Jason Balayev (cpp)