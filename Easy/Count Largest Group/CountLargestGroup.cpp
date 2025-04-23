class Solution {
public:
    int countLargestGroup(int n) {
        int counts[37]={0};
        for (int i =0; i<=n; i++){
            int num=i;
            int sum=0;
            while (num>0){
                sum+=num%10;
                num/=10;
            }
            counts[sum]++;
        }
        int maxCount=0;
        for (int i=0; i<=36; i++){
            if (counts[i]>maxCount){
                maxCount=counts[i];
            }
        }
        int res=0;
        for (int i=1; i<=36; i++){
            if (counts[i]==maxCount){
                res++;
            }
        }
        return res;
    }
};

//QED
//Problem 1399 (Easy of Count Largest Group) - Jason Balayev (cpp  
