class Solution {
public:
    string removeStars(string s) {
        string res;
        for (char c:s){
            if (c=='*'){
                res.pop_back();
            } else{
                res.push_back(c);
            }
        }
        return res;
    }
};

//QED
//Problem 2390 (Medium of Removing Stars From A String) - Jason Balayev (cpp)