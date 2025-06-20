using namespace std;
class Solution {
public:
    int maxDistance(string s, int k) {
        long long cntN=0,cntS=0,cntE=0,cntW=0;
        long long best=0;
        long long n=s.size();
        for(long long i=0;i<n;i++){ 
            switch(s[i]){
                case 'N':++cntN;break;
                case 'S':++cntS;break;
                case 'E':++cntE;break;
                case 'W':++cntW;break;
            }
            long long len=i+1;
            long long m=std::min(cntN,cntS)+std::min(cntE,cntW);
            long long ifPossible=len-2LL*std::max(0LL,m-(long long)k);
            best=std::max(best,ifPossible);
        }
        return static_cast<int>(best);
    }
};

//QED 
//Problem 3443 (Medium of Maximum Manhattan Distance After K Changes) - Jason Balayev (cpp)