#include<algorithm>
#include<iostream>
class Solution {
public:
    int findKthNumber(int n, int k) {
        long long prefix=1;
        k--;
        while(k>0){
            long long howMany=countUnderPrefix(prefix,n);
            if(k>=howMany){
                k-=howMany;
                prefix++;
            }else{
                prefix*=10;
                k--;
            }
        }
        return static_cast<int>(prefix);
    }
private:
    long long countUnderPrefix(long long prefix,int limit){
        long long cnt=0;
        long long first=prefix;
        long long next=prefix+1;
        while(first<=limit){
            cnt+=min(next,static_cast<long long>(limit)+1)-first;
            first*=10;
            next*=10;
        }
        return cnt;
    }
};