class Solution {
public:
    int minMaxDifference(int num) {
        int mx=0,mn=0;
        int temp=num;
        int dig[10];
        int len=0;
        while(temp){
            dig[len++]=temp%10;
            temp/=10;
        }
        int oldMax=-1;
        for(int i=len-1;i>=0;i--){
            if(dig[i]!=9){
                oldMax=dig[i];
                break;
            }
        }
        for(int i=len-1;i>=0;i--){
            int d=dig[i];
            if(d==oldMax)d=9;
            mx=mx*10+d;
        }
        if(dig[len-1]==1){
            int oldMin=-1;
            for(int i=len-2;i>=0;i--){
                if(dig[i]!=0&&dig[i]!=1){
                    oldMin=dig[i];
                    break;
                }
            }
            for(int i=len-1;i>=0;i--){
                int d=dig[i];
                if(d==1)d=0;
                mn=mn*10+d;
            }
        }else{
            int first=dig[len-1];
            for(int i=len-1;i>=0;i--){
                int d=dig[i];
                if(d==first)d=0;
                mn=mn*10+d;
            }
        }
        return mx-mn;
    }
};

//QED
//Problem 2566 (Easy of Maximum Difference By Remapping A Digit) - Jason Balayev (cpp)