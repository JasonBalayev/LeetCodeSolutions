public class Solution {
    public int FirstUniqChar(string s) {
        int[]count = new int[26];
        foreach(char c in s)
            count[c-'a']++;
        for(int i=0; i<s.Length;i++)
            if (count[s[i]-'a']==1)
                return i;
            return -1;
    }
}

//QED
//Problem 387 (Easy of First Unique Character In A String) - Jason Balayev (csharp)
