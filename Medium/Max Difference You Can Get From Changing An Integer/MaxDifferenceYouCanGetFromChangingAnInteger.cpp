class Solution {
public:
    int maxDiff(int num) {
        int d[10];
        int n=0;
        int t=num;
        while(t){
            d[n++]=t%10;
            t/=10;
        }
        if(n==0)d[n++]=0;
        auto build=[&](int oldDig, int newDig){
            long long res=0;
            for(int i=n-1;i>=0;--i){
                int dig=d[i];
                if(dig==oldDig)dig=newDig;
                res=res*10+dig;
            }
            return (int)res;
        };
        int oldA=-1;
        for(int i=n-1;i>=0;--i){
            if(d[i]!=9){oldA=d[i];break;}
        }
        int a=(oldA==-1)?num:build(oldA,9);
        int firstDig=d[n-1];
        int oldB=-1,newB=0;
        if(firstDig!=1){
            oldB=firstDig;
            newB=1;
        }else{
            for(int i=n-2;i>=0;--i){
                if(d[i]!=0&&d[i]!=1){oldB=d[i];break;}
            }
            if(oldB==-1){
                return a-num;
            }
            newB=0;
        }
        int b=build(oldB,newB);
        return a-b;
    }
};

//QED
//Problem 1432 (Medium of Max Difference You Can Get From Changing An Integer) - Jason Balayev (cpp)