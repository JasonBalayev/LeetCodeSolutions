class Solution {
public:
    int minFlips(int a, int b, int c) {
        int flips=0;
        while(a||b||c){
            int bitA=a&1;
            int bitB=b&1;
            int bitC=c&1;
            if(bitC==1){
                if(bitA==0&&bitB==0){
                    flips++;
                }
            }else{
                if(bitA==1)flips++;
                if(bitB==1)flips++;
            }
            a>>=1;
            b>>=1;
            c>>=1;
        }
        return flips;
    }
};

//QED
//Problem 1318 (Medium of Minimum Flips To Make A Or B Equal To C) - Jason Balayev (cpp)