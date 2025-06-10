class Solution {
public:
    int maxDifference(string s) {
        int freq[26]={0};
        for(int i =0;i<s.length();i++){
            freq[s[i]-'a']++;
        }
        int maxOdd=-1;
        int minEven=999999;
        for(int i=0;i<26;i++){
            if(freq[i]>0){
                if(freq[i]%2==1){
                    if(freq[i]>maxOdd){
                        maxOdd=freq[i];
                    }
                }else{
                    if(freq[i]<minEven){
                        minEven=freq[i];
                    }
                }
            }
        }
        return maxOdd-minEven;
    }
};

//QED
//Problem 3442 (Easy of Maximum Difference Between Even And Odd Frequency I) - Jason Balayev (cpp)