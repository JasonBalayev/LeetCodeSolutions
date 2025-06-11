class Trie {
    int children[1000000][26];
    bool isEnd[100000];
    int nodeAmt;
public:
    Trie() {
        nodeAmt=1;
        for(int i=0;i<26;i++){
            children[0][i]=-1;
        }
        isEnd[0]=false;
    }
    void insert(string word) {
        int curr=0;
        for(int i=0;i<word.length();i++){
            int idx=word[i]-'a';
            if(children[curr][idx]==-1){
                children[curr][idx]=nodeAmt;
                for(int j=0;j<26;j++){
                    children[nodeAmt][j]=-1;
                }
                isEnd[nodeAmt]=false;
                nodeAmt++;
            }
            curr=children[curr][idx];
        }
        isEnd[curr]=true;
    }
    bool search(string word) {
        int curr=0;
        for(int i=0;i<word.length();i++){
            int idx=word[i]-'a';
            if(children[curr][idx]==-1)return false;
            curr=children[curr][idx];
        }
        return isEnd[curr];
    }
    
    bool startsWith(string prefix) {
        int curr=0;
        for(int i=0;i<prefix.length();i++){
            int idx=prefix[i]-'a';
            if(children[curr][idx]==-1)return false;
            curr=children[curr][idx];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

//QED
//Problem 208 (Medium of Implement Trie (Prefix Tree)) - Jason Balayev (cpp)