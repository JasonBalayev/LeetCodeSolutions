class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.length()!=word2.length()) {
            return false;
        }
        vector<int> count1(26,0);
        vector<int> count2(26,0);
        vector<bool> present1(26,false);
        vector<bool> present2(26,false);
        
        for (char c:word1){
            count1[c-'a']++;
            present1[c-'a']=true;
        }
        for (char c:word2){
            count2[c-'a']++;
            present2[c-'a']=true;
        }
        for (int i=0; i<26; i++){
            if (present1[i]!=present2[i]){
                return false;
            }
        }
        sort(count1.begin(),count1.end());
        sort(count2.begin(),count2.end());
        return count1==count2;
    }
};

//QED
//Problem 1657 (Medium of Determine If Two Strings Are Close) - Jason Balayev (cpp)  