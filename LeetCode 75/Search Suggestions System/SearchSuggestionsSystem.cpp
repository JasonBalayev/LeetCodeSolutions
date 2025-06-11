class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        sort(products.begin(),products.end());
        vector<vector<string>>ans;
        string s="";
        for(int i=0;i<searchWord.length();i++){
            s+=searchWord[i];
            vector<string>temp;
            for(int j=0;j<products.size()&&temp.size()<3;j++){
                if(products[j].substr(0,s.length())==s){
                    temp.push_back(products[j]);
                }
            }
            ans.push_back(temp);
        }
        return ans;
    }
};

//QED
//Problem 1268 (Medium of Search Suggestions System) - Jason Balayev (cpp)