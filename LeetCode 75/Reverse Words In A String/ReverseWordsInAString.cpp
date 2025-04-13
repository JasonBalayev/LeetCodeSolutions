class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word, res;

        while(ss>>word) {
            res = word+(res.empty() ? "":" ") + res;
        }
        return res;
    }
};


//QED
//Problem 151 (Medium of Reverse Words in a String) - Jason Balayev (cpp)