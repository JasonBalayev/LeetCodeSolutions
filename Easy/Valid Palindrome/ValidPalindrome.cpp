#include<string>
#include<cctype>
using namespace std;
class Solution {
public:
    bool isPalindrome(string s) {
        string t;
        for(char c:s){
            if(isalnum(static_cast<unsigned char>(c)))
                t.push_back(tolower(static_cast<unsigned char>(c)));
        }
        int i=0,j=static_cast<int>(t.size())-1;
        while(i<j){
            if(t[i]!=t[j]) return false;
            ++i;
            --j;
        }
        return true;
    }
};