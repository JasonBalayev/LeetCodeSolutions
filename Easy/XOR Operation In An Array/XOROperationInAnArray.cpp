class Solution {
public:
    int xorOperation(int n, int start) {
        int result = 0;
        for (int i = 0; i < n; i++) {
            result ^= start + 2 * i;
        }
        return result;
    }
};

//QED
//Problem 1486 (Easy Of XOR Operation In An Array) - Jason Balayev (cpp)
