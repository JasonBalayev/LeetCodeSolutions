class Solution {
public:
    int maxVowels(string s, int k) {
        auto vowel =[](char c) -> bool {
            return ((1<<(c-'a'))&((1<<('a'-'a')) | (1<< ('e'-'a')) | 
                                        (1<<('i'-'a'))|(1<<('o'-'a')) | 
                                        (1 <<('u'-'a'))))!= 0;
        };
        int maxCount=0;
        int currCount=0;

        for (int i=0; i<k; i++) {
            currCount += vowel(s[i]);
        }
        maxCount = currCount;
        if (maxCount==k) return k;
        for (int i=k; i<s.length(); i++) {
            currCount+=vowel(s[i])-vowel(s[i-k]);
            maxCount=max(maxCount,currCount);
            if (maxCount==k) return k;
        }
        return maxCount;
    }
};

//QED
//Problem 1456 (Medium of Maximum Number of Vowels In A Substring Of Given Length) - Jason Balayev (cpp)