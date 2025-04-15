class Solution {
public:
    string reverseVowels(string s) {
        string vowels = "aeiouAEIOU";
        int left = 0;
        int right = s.length()-1;

        while (left<right) {
            while (left<right && vowels.find(s[left])==string::npos) {
                left++;
            }
            while (left<right && vowels.find(s[right])==string::npos) {
                right--;
            }
            if (left<right) {
                swap(s[left], s[right]);
                right--;
                left++;
            }
        }
        return s;
    }
};

//QED
//Problem 345 (Easy of Reverse Vowels of a String) - Jason Balayev (cpp)

