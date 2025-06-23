class Solution {
public:
    long long kMirror(int k, int n) {
        long long sum=0;
        int found=0;
        for(int len=1; found<n;++len){
            int half=(len+1)/2;
            long long start=1;
            for(int i=1;i<half;++i)start*=10;
            long long end=start*10-1;
            for(long long half=start;half<=end&&found<n;++half){
                long long pal=buildPalindrome(half,len%2);
                if(isKPalindrome(pal,k)){
                    sum+=pal;
                    ++found;
                }
            }
        }
        return sum;
    }
private:
    long long buildPalindrome(long long left,bool isOdd){
        long long res=left;
        if(isOdd)left/=10;
        while(left>0){
            res=res*10+(left%10);
            left/=10;
        }
        return res;
    }
    bool isKPalindrome(long long num,int k){
        int dig[64];
        int len=0;
        while(num>0){
            dig[len++]=static_cast<int>(num%k);
            num/=k;
        }
        int i=0,j=len-1;
        while(i<j){
            if(dig[i++]!=dig[j--])return false;
        }
        return true;
    }
};

//QED
//Problem 2081 (Hard of Sum Of K-Mirror Numbers) - Jason Balayev (cpp)