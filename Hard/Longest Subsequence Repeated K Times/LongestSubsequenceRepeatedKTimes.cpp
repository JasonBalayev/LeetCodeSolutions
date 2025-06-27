class Solution {
public:
    bool isValid(const string&seq,const string&s,int k) {
        if(seq.empty())return true;
        int idx=0;
        int repeated=0;
        for(char ch:s) {
            if(ch==seq[idx]) {
                ++idx;
                if(idx==(int)seq.size()){
                    ++repeated;
                    if(repeated==k)return true;
                    idx=0;
                }
            }
        }
        return false;
    }
    bool compositionOk(const string&seq,const array<int,26>&freq,int k) {
        array<int,26>cnt{};
        for(char ch:seq)cnt[ch-'a']++;
        for(int i=0;i<26;++i)
            if(cnt[i]*k>freq[i])return false;
        return true;
    }
    string longestSubsequenceRepeatedK(string s, int k) {
        const int n=s.size();
        if(k==1)return s;
        array<int,26>freq{};
        for(char ch:s)freq[ch-'a']++;
        queue<string>q;
        q.push("");
        string best="";

        while(!q.empty()) {
            string cur=q.front();
            q.pop();
            for(char c='z';c>='a';--c) {
                if(freq[c-'a']<k)continue;
                string next=cur+c;
                if(!compositionOk(next,freq,k))continue;
                if(isValid(next,s,k)) {
                    q.push(next);
                    if(next.size()>best.size()||(next.size()==best.size()&&next>best)){
                        best=next;
                    }
                }
            }
        }
        return best;
    }
};

//QED
//Problem 2014 (Hard of Longest Subsequence Repeated K Times) - Jason Balayev (cpp)