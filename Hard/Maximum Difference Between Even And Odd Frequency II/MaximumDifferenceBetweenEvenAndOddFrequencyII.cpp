#include <bits/stdc++.h>
using namespace std;
class Solution {
    struct Fenwick {
        int n;
        vector<int> bit;
        Fenwick(int _n,int INF):n(_n),bit(_n+1,INF){}
        void update(int idx,int val){
            for(++idx;idx<=n;idx+=idx&-idx) bit[idx]=min(bit[idx],val);
        }
        int query(int idx){
            int res=INT_MAX;
            for(++idx;idx>0;idx-=idx&-idx) res=min(res,bit[idx]);
            return res;
        }
    };
public:
    int maxDifference(string s,int k) {
        const int INF=1e9;
        int n=(int)s.size();
        vector<array<int,5>> pref(n+1);
        pref[0].fill(0);
        for(int i=0;i<n;i++){
            pref[i+1]=pref[i];
            pref[i+1][s[i]-'0']++;
        }
        int ans = -INF;
        for(int a=0;a<5;a++){
            for(int b=0;b<5;b++) if(a!=b){
                Fenwick ft[2][2]={{Fenwick(n,INF),Fenwick(n,INF)},{Fenwick(n,INF),Fenwick(n,INF)}};
                for(int idx=0;idx<=n;idx++){
                    if(idx-k>= 0){
                        int l=idx-k;
                        int pa=pref[l][a]&1;
                        int pb=pref[l][b]&1;
                        int diff=pref[l][a]-pref[l][b];
                        int cntB=pref[l][b];
                        ft[pa][pb].update(cntB,diff);
                    }
                    int paR=pref[idx][a]&1;
                    int pbR=pref[idx][b]&1;
                    int neededPa=paR^1;
                    int neededPb=pbR;
                    int cntB=pref[idx][b];
                    if(cntB==0) continue;
                    int bestLeft=ft[neededPa][neededPb].query(cntB-1);
                    if(bestLeft!=INT_MAX){
                        int curDiff=(pref[idx][a]-pref[idx][b])-bestLeft;
                        if(curDiff>ans)ans=curDiff;
                    }
                }
            }
        }
        return ans==-INF?-1:ans;
    }
};

//QED
//Problem 3345 (Hard of Maximum Difference Between Even And Odd Frequency II) - Jason Balayev (cpp)