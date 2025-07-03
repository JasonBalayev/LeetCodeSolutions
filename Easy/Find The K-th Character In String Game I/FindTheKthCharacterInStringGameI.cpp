class Solution {
public:
    char kthCharacter(int k) {
        string w="a";
        while((int)w.size()<k){
            string t=w;
            for(char &ch:t){
                ch=(ch=='z')?'a':ch+1;
            }
            w+=t;
        }
        return w[k-1];
    }
};

//QED
//Problem 3304 (Easy of Find The K-th Character In String Game I) - Jason Balayev (cpp)