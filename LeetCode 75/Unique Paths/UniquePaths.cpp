class Solution {
public:
    int uniquePaths(int m, int n) {
        long long r=1;
        for(int i=0;i<m-1;i++){
            r=r*(n+i)/(i+1);
        }
        return r;
    }
};