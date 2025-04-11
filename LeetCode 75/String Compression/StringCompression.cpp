class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        if (n <= 1) return n;
        
        int writeIdx = 0, count = 1;
        
        for (int i = 1; i <= n; i++) {
            if (i < n && chars[i] == chars[i-1]) {
                count++;
            } else {
                chars[writeIdx++] = chars[i-1];
                
                if (count > 1) {
                    for (char c : to_string(count))
                        chars[writeIdx++] = c;
                }
                count = 1;
            }
        }
        
        return writeIdx;
    }
};

//QED
//Problem 443 (Medium of String Compression) - Jason Balayev (cpp)