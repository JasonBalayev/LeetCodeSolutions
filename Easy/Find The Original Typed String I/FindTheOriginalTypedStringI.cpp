class Solution {
public:
    int possibleStringCount(string word) {
        int total=1;
        int curr=1;
        for(size_t idx=1;idx<word.size();++idx){
            if(word[idx]==word[idx-1]){
                ++curr;
            }else{
                if(curr>1){
                    total+=curr-1;
                }
                curr=1;
            }
        }
        if(curr>1){
            total+=curr-1;
        }
        return total;
    }
};

//QED
//Problem 3330 (Easy of Find The Original Typed String I) - Jason Balayev (cpp)